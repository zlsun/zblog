# zblog

A simple blog developed with Django.

## Requirements

- Python 2.7
- Django
- django-suit
- django-markdown-deux
- django-pagedown
- [duoshuo-python-sdk](https://github.com/duoshuo/duoshuo-python-sdk)

## Guide

1. Clone this project.

    ```sh
    git clone https://github.com/zlsun/zblog && cd zblog
    ```

2. Install all requirements, you may need `sudo` to execute this command.

    ```sh
    pip install -r requirements.txt
    ```

3. Create database. You will be asked to create an account.

    ```sh
    python manager.py syncdb
    ```

4. Run server.

    ```sh
    python manager.py runserver
    ```

5. Initialize blog.

    Open `http://127.0.0.1/admin`, login with the account created in step 3.
    Create a `blog` under `Blogs` table. Then, add some articles in `Entrys` table.

6. Open `http://127.0.0.1/zblog` in browser to visit the blog.

## Screenshots

<table>
    <tr>
        <td width="30%">
            <a href="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/1.png">
                <img src="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/1.png" width="100%">
            </a>
        </td>
        <td width="30%">
            <a href="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/2.png">
                <img src="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/2.png" width="100%">
            </a>
        </td>
        <td width="30%">
            <a href="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/3.png">
                <img src="https://raw.githubusercontent.com/zlsun/screenshots/master/zblog/3.png" width="100%">
            </a>
        </td>
    <tr>
</table>

## License

[MIT License](LICENSE)

