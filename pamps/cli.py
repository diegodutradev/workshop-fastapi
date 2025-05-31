import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select
from pamps.security import HashedPassword

from .config import settings
from .db import engine
from .models import User

main = typer.Typer(name="Pamps CLI")


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "User": User,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(
        argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars
        )
    except ImportError:
        import code
        
        code.InteractiveConsole(_vars).interact()


@main.command()
def user_list():
    """Lists all users"""
    table = Table(title="Pamps users")
    fields = ["username", "email"]
    for header in fields:
        table.add_column(header, style="magenta")

    with Session(engine) as session:
        users = session.exec(select(User))
        for user in users:
            table.add_row(user.username, user.email)

    Console().print(table)


@main.command()
def create_user(email: str, username: str, password: str):
    """Create user"""
    hashed_pw = HashedPassword.validate(password)  # <- executa o hash manualmente
    user = User(email=email, username=username, password=hashed_pw)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        typer.echo(f"created {username} user")
