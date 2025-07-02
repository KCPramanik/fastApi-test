TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:Nrcf@21@localhost:5432/test_db"
    },
    "apps": {
        "models": {
            "models": ["app.models"],  
            "default_connection": "default",
        },
    },
}
