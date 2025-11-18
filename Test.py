import os
from volcenginesdkarkruntime import Ark

# 初始化Ark客户端
# 建议将API Key存储在环境变量中，这里为了演示直接写在代码里
client = Ark(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key='905f6087-0cc0-4d6a-824c-1c0fec073594',  # 替换成你的API Key
)


def chat_with_ai(text_input):
    """
    与AI模型进行文本对话

    参数:
        text_input: 用户输入的文本

    返回:
        AI模型的回答文本
    """
    # 发送请求给AI模型
    completion = client.chat.completions.create(
        model="doubao-seed-1-6-251015",  # 使用的模型ID
        messages=[
            {
                "role": "user",
                "content": text_input  # 纯文本输入
            }
        ],
        reasoning_effort="low",  # 推理强度：low/medium/high
    )

    # 返回AI的回答
    return completion.choices[0].message.content


def chat_with_ai_streaming(text_input):
    """
    与AI模型进行文本对话（流式输出）
    适合长文本回答，可以实时看到内容

    参数:
        text_input: 用户输入的文本
    """
    print("AI正在思考中...")

    # 发送请求给AI模型，开启流式输出
    stream = client.chat.completions.create(
        model="doubao-seed-1-6-251015",
        messages=[
            {
                "role": "user",
                "content": text_input
            }
        ],
        reasoning_effort="medium",
        stream=True,  # 开启流式输出
    )

    # 实时打印AI的回答
    print("AI回答：", end="")
    for chunk in stream:
        if chunk.choices:
            print(chunk.choices[0].delta.content or "", end="")
    print()


# --- 使用示例 ---
if __name__ == "__main__":
    print("=== 文本AI对话演示 ===")

    # 1. 简单对话（一次性获取完整回答）
    print("\n1. 简单对话模式：")
    user_input = "你好，介绍一下自己"
    print(f"用户：{user_input}")
    response = chat_with_ai(user_input)
    print(f"AI：{response}")

    # 2. 流式对话（实时获取回答）
    print("\n2. 流式对话模式：")
    user_input = "请详细解释一下人工智能的发展历程"
    print(f"用户：{user_input}")
    chat_with_ai_streaming(user_input)

    # 3. 用户交互模式
    print("\n3. 交互式对话（输入 'exit' 退出）：")
    while True:
        user_input = input("你：")
        if user_input.lower() == 'exit':
            print("对话结束")
            break
        if not user_input.strip():
            print("请输入有效内容")
            continue

        print("AI：", end="")
        # 使用流式输出，让回答更流畅
        stream = client.chat.completions.create(
            model="doubao-seed-1-6-251015",
            messages=[{"role": "user", "content": user_input}],
            stream=True
        )
        for chunk in stream:
            if chunk.choices:
                print(chunk.choices[0].delta.content or "", end="")
        print("\n")