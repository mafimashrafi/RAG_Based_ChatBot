with open("Config/prompt.txt", "r") as f:
    system_prompt = f.readlines()

def get_final_prompt(context, query):
    prompt = f"{system_prompt}\n\n {context}\n\n {query}"

    return prompt