# LLaMa-Factory 支持两种自定义数据集
## 1.alpaca格式 https://github.com/open-chinese/alpaca-chinese-dataset
https://llamafactory.readthedocs.io/zh-cn/latest/getting_started/data_preparation.html
```
[  
  {  
    "en_instruction":"用户指令（选填）", 
    "instruction": "用户指令（必填）",  
    "input": "用户输入（选填）",  
    "output": "模型回答（必填）",  
    "system": "系统提示词（选填）",  
    "history": [  
      ["第一轮指令（选填）", "第一轮回答（选填）"],  
      ["第二轮指令（选填）", "第二轮回答（选填）"]  
    ]  
  }  
]
```
如：
```
{
    "en_instruction": "Conver the temperature from Fahrenheit to Celsius.",
    "instruction": "将温度从华氏度调到摄氏度。",
    "en_input": "94F",
    "input": "94F",
    "en_output": "34.4C",
    "output": "34.4摄氏度"
}
```
单轮训练数据集格式：
```
{  
  "instruction": "写一个有效的比较语句",  
  "input": "篮球和足球",  
  "output": "篮球和足球都是受欢迎的运动。"  
}
```

多轮数据集格式：
```
{  
  "instruction": "谢谢",  
  "input": "",  
  "output": "不用谢! 很高兴我提供的信息能够帮助到你! 如果还有什么其他问题也可以向我提问。",  
  "history": [  
    [  
      "请你给我写一个面试准备计划，我想要去面试微软的程序员岗位",  
      "首先，你可以去微软官网寻找招聘信息并申请面试。\n其次，您可以在社交媒体平台寻找微软公司对程序员的面试问题，并做好准备。\n最后，您可以自己对面试过程进行模拟，熟悉话题并减少紧张感。\n我希望你能面试成功。"  
    ]  
  ]  
}

```
## 2. sharegpt格式
```
{
  "conversations": [
    {
      "from": "human",
      "value": "你好，我出生于1990年5月15日。你能告诉我我今天几岁了吗？"
    },
    {
      "from": "function_call",
      "value": "{\"name\": \"calculate_age\", \"arguments\": {\"birthdate\": \"1990-05-15\"}}"
    },
    {
      "from": "observation",
      "value": "{\"age\": 31}"
    },
    {
      "from": "gpt",
      "value": "根据我的计算，你今天31岁了。"
    }
  ],
  "tools": "[{\"name\": \"calculate_age\", \"description\": \"根据出生日期计算年龄\", \"parameters\": {\"type\": \"object\", \"properties\": {\"birthdate\": {\"type\": \"string\", \"description\": \"出生日期以YYYY-MM-DD格式表示\"}}, \"required\": [\"birthdate\"]}}]"
}
```
数据参考：
https://blog.csdn.net/python12345678_/article/details/140346926
