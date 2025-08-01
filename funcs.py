def deepseekquery(userprom,opt_sysprom, env = "OPENAI_API_KEY"):
    from openai import OpenAI
    import os
    api_key = os.getenv(env)
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": opt_sysprom},
            {"role": "user", "content": userprom},
        ],
        stream=False
    )

    extracted_response = response.choices[0].message.content
    return extracted_response

def casRecord(userprom:str,opt_sysprom = "请模拟一个正在写学校社团活动记录的人，你需要把输入的做的一些事的中文或英文短语包括活动日期扩展成一篇最少90词，最多110词的英文活动记录，不需要标题，并在末尾标上xx words。目前用户有两个社团：数学社Math Club/信息化社Computerization，前者是与数学理论相关，后者是代码实现相关，信息化社中，用户可能会反复提到两个项目：Enspire和c13n，前者是我们开发的社团管理系统，后者是我们的社刊。输出时直接输出英文活动记录即可，不要其他内容。") -> str:
    return deepseekquery(userprom,opt_sysprom)


userprompt = "2025.3.6, debug the Enspire project, improve its robustness while checking club list, work for the optimization in style of the c13n website"

def clubReflection(userprom:str,opt_sysprom = "请模拟一个正在写学校社团活动反思的人，你需要把输入的做的一些事的中文或英文短语包括活动日期扩展成一篇最少600词最多700词的大型英文反思文章，不需要标题，并在末尾标上xx words，与真实词数要严格对应！，反思文章需要包含以下2-3个主题，不要写成流水账  1. Awareness  2. Challenge  3. Initiative  4. Collaboration 5. Commitment  6. New Skills。目前用户有两个社团：数学社Math Club/信息化社Computerization，前者是与数学理论相关，后者是代码实现相关，信息化社中，用户可能会反复提到两个项目：Enspire和c13n，前者是我们开发的社团管理系统，后者是我们的社刊。输出时直接输出英文活动记录即可，不要其他内容。") -> str:
    return deepseekquery(userprom,opt_sysprom)