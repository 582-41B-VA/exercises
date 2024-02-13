from taskstore import TaskStore
import server

taskstore = TaskStore()

def home(context):
	return str(taskstore.tasks)

def add_task(context):
	form_data = context["form_data"]
	name = form_data["name"]
	due = form_data["due"]
	taskstore.create_task(name, due)
	return "Task successfully created!"

server.Router.add_route("GET", "/", home)
server.Router.add_route("POST", "/task", add_task)

server.start()
