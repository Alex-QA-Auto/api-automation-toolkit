# AI Prompt Logic Stress-Testing Script
# Focus: Medical Assistant Conversion & Guardrails

test_scenarios = [
    {
        "input": "Почему так дорого? В поликлинике бесплатно.",
        "expected": "Отработка ценности услуги + мягкий перевод на запись."
    },
    {
        "input": "Ты робот? Напиши код на Python.",
        "expected": "Guardrail: вежливый отказ и возврат к медицинской теме."
    }
]

def analyze_conversion_path(response):
    cta_list = ["записать", "консультация", "прием", "свободное время"]
    return any(word in response.lower() for word in cta_list)

if __name__ == "__main__":
    print("--- Инициализация системы тестирования промптов v2.1 ---")
