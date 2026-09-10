from datetime import date


def get_repo_visibility(is_private: bool) -> str:
    """Возвращает текстовый статус видимости репозитория."""
    if is_private:
        return 'Репозиторий приватный'
    return 'Репозиторий публичный'


def is_project_archived(is_archived: bool) -> bool:
    """Проверяет, находится ли проект в архиве."""
    if is_archived:
        return True
    return False


def has_role(
    member_role: str,
    required_role: str,
) -> bool:
    """Проверяет, достаточно ли роли участника для действия."""
    if member_role == 'owner':
        return True
    if member_role == required_role:
        return True
    return False


def mask_clone_url(clone_url: str) -> str:
    """Маскирует URL клонирования, оставляя видимыми крайние символы."""
    if len(clone_url) < 16:
        return '***'
    prefix = clone_url[0:12]
    suffix = clone_url[-7:]
    return prefix + '...' + suffix


user_name = 'Кирилл Челышев'
project_name = 'Учебный портал'
repo_name = 'portal-backend'
clone_url = 'https://git.example.com/portal-backend.git'
is_private = True
is_archived = False
member_role = 'developer'
required_role = 'developer'
created_date = date(2026, 1, 15)
today = date(2026, 9, 10)

print(f'Пользователь: {user_name}')
print(f'Проект: {project_name}')
print(f'Репозиторий: {repo_name}')
print(f'URL: {mask_clone_url(clone_url)}')
print(get_repo_visibility(is_private))

if is_project_archived(is_archived):
    print('Проект в архиве. Изменения запрещены.')
else:
    print('Проект активен.')

if has_role(member_role, required_role):
    print('У участника есть право на запись в репозиторий.')
else:
    print('Недостаточно прав для записи в репозиторий.')
