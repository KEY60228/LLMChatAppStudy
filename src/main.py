import openai
import json

# 関数定義
def get_current_weather(location, unit="celcius"):
  weather_info = {
    "location": location,
    "temperature": 25,
    "unit": unit,
    "forecast": ["sunny", "windy"],
  }
  return json.dumps(weather_info)

# GPTで使用可能な関数情報の定義
functions = [
  {
    "name": "get_current_weather",
    "description": "Get the current weather in a given location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city and state, e.g. Tokyo",
        },
        "unit": {
          "type": "string",
          "enum": ["celcius", "fahrenheit"],
        },
      },
      "required": ["location"]
    },
  },
]

# メッセージ
messages = [
  {"role": "user", "content": "What's the weather in Tokyo?"},
]

# リクエスト
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages,
  functions=functions,
)

# 初回のレスポンス
response_message = response["choices"][0]["message"]

# 関数の呼び出し
available_functions = {
  "get_current_weather": get_current_weather,
}
function_name = response_message["function_call"]["name"]
function_to_call = available_functions[function_name]
function_args = json.loads(response_message["function_call"]["arguments"])
function_response = function_to_call(
  location=function_args.get("location"),
  unit=function_args.get("unit"),
)

# メッセージの追加
messages.append(response_message)
messages.append(
  {
    "role": "function",
    "name": function_name,
    "content": function_response,
  }
)

# 再度リクエスト
second_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages,
)

print(second_response["choices"][0]["message"]["content"])
