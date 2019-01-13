# Определение победителя

## Фильтрует людей
* которые подписались на аккаунт
* упомянули хотя бы одного друга
* лайкнули пост


## Требования
  
  * python3
  * установка зависимостей
  ```pip install -r requirements.txt```
  * иметь учетную запись в инстаграм
  * записать логин пароль в .env файл:
  ```
  login=...
  pass=...
  ```

  
  Пример:
```bash
$ python main.py -u <url поста> -n <имя аккаунта>
Пользователи выполнившие условия:
[...]

```


## Цель проекта
Код написан в учебных целях. Учебный курс для веб-разработчиков - [dvmn.org](https://dvmn.org)
