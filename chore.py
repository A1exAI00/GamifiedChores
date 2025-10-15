import click
import yaml

@click.group()
def cli():
    pass


@cli.command()
@click.argument("file", default="config.yaml")
def show(file):
    with open(file, "r") as file:
        config = yaml.safe_load(file)

    if not config:
        raise Exception(f"{file}: File not found")
    
    click.echo(str(config))
    return


@cli.command()
@click.argument("file", default="config.yaml")
def generate_template(file):
    with open(file, "r") as file:
        config = yaml.safe_load(file)

    if not config:
        raise Exception(f"{file}: File not found")

    chores = config["CHORES_LIST"]
    weekdays = config["WEEKDAYS_LIST"]
    users = config["USERS_LIST"]

    users_str = ", ".join(users)

    template = ["%YAML 1.2", "---"]
    for chore, _type in chores:
        this = []
        this.append("-")
        this.append(f"  chore: {chore}")
        this.append(f"  type: {_type}")
        for weekday in weekdays:
            this.append(f"  {weekday}: [{users_str}]")
        this_str = "\n".join(this)
        template.append(this_str)

    template_str = "\n".join(template)

    with open("template.yaml", "w") as file:
        file.write(template_str)

    return




cli.add_command(generate_template)
# cli.add_command(dropdb)

if __name__ == "__main__":
    cli()
