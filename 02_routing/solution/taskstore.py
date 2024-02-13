"""Task store for a tasks management application."""

class TaskStore:
    """A store of tasks."""

    def __init__(self):
        self.tasks = {}
        self._counter = 1

    def _create_uid(self):
        """Return a new UID (int)."""
        uid = self._counter
        self._counter += 1
        return uid

    def create_task(self, name, due=None):
        """Create a new task with the given name and due date.

        Args:
            name (str): Name of the task.
            due (str): Optional due date.

        Returns:
            Copy of the newly created task (dict).
        """
        uid = self._create_uid()
        new_task = {"uid": uid, "name": name, "due": due}
        self.tasks[uid] = new_task
        return new_task

    def get_task(self, uid):
        """Return the task associated with the given uid.

        Arg:
            uid (int): UID of the task to retreive.
        """
        return self.tasks[uid]

    def delete_task(self, uid):
        """Delete the task assoicated with the given uid.

         Arg:
            uid (int): UID of the task to delete.

        Returns:
            Copy of the deleted task (dict).
        """
        return self.tasks.pop(uid)
