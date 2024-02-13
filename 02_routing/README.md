# Exercise: Routing

For this exercise, you are asked to decouple the server and the logic of
your task management application. Remove any code related to your task
management application in the server module, and vice versa. It should
be possible to use the server with any other application.

To do so, you will need to change the server module so that you can add
routes and start the server from other modules. To make sure the
requirements are met, you are encouraged to create a third module named
"app" from which you define the routes and start the server.

## Tips

-   Start with static routes (e.g., "/", "/task"). Once you have figured
    out how to add static routes, modify the code so you can also add
    dynamic routes (e.g., "/task/1", "/task/2", "/task/n").
-   Take a look at JavaScript's `EventTarget` interface. How does the
    `addEventListener` method work?
-   Take a look at [regular expressions][].

[regular expressions]: https://docs.python.org/3/howto/regex.html
