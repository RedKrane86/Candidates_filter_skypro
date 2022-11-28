import json


def load_candidates():
    """Загружает данные из файла json"""
    with open("candidates.json", "r", encoding="utf8") as file:
        return json.load(file)


def get_all():
    """Показывает всех кандидатов"""
    return load_candidates()
    

def get_by_pk(pk):
    """Возвращает кондидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return None


def get_by_skill(skill_name):
    """Возвращаетт кандидатов по навыку"""
    candidates_list = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates_list.append(candidate)
    return candidates_list

