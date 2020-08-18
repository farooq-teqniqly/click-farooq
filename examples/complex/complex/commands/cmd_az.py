from click import Context

from complex.cli import pass_environment, Environment

import click


class EventHubCollection:
    def __init__(self):
        self.event_hubs = []


pass_event_hub_collection = click.make_pass_decorator(EventHubCollection)


@click.group(short_help="Azure CLI commands.")
@click.pass_context
def cli(ctx: Context):
    ctx.obj = EventHubCollection()


@cli.group()
def eventhubs():
    pass


@eventhubs.command("create", short_help="Create an event hub.")
@click.argument("name")
@pass_event_hub_collection
@pass_environment
def eventhubs_create(env: Environment, ehc: EventHubCollection, name: str):
    ehc.event_hubs.append(name)
    env.log(f"Created eventhub '{name}'.")


@eventhubs.command("delete", short_help="Delete an event hub.")
@click.argument("name")
@pass_event_hub_collection
@pass_environment
def eventhubs_deleted(env: Environment, ehc: EventHubCollection, name: str):
    ehc.event_hubs.remove(name)
    env.log(f"Deleted eventhub '{name}'.")


@eventhubs.command("list", short_help="List event hubs.")
@pass_event_hub_collection
@pass_environment
def eventhubs_list(env: Environment, ehc: EventHubCollection):
    env.log(ehc.event_hubs)


@eventhubs.command("show", short_help="Show an event hub's details.")
@click.argument("name")
@pass_event_hub_collection
@pass_environment
def eventhubs_show(env: Environment, ehc: EventHubCollection, name: str):
    env.log(filter(lambda n: n == name, ehc.event_hubs))
