### Aerich - Info

1. [Aerich - doc](https://github.com/tortoise/aerich)
2. [Documentation](https://ashfakmeethal.medium.com/tortoise-orm-migrations-with-aerich-5ebb7238bed5)
3. [Tortoise - Aerich](https://tortoise-orm.readthedocs.io/en/latest/migration.html)

#### Aerich - error and their solution

1. Error while importing configuration module: No module named 'app' #188
    - Version: 0.5.6
    - Error:  `aerich init-db`
    - Decision: `pip install aerich==0.5.5`
    - Info:
        - [Github](https://github.com/tortoise/aerich/issues/188)
        - [StackOverflow](https://stackoverflow.com/questions/68764476/error-while-importing-configuration-module-no-module-named-app-aerich)

2. tortoise.exceptions.ConfigurationError: No DB associated to model
    - addition `"aerich.models"`
    - example schema
    ```python
    TORTOISE_ORM = {
        'connections': {
            "default": "postgres://admin:admin@localhost:5432/aiogram_django"
        },
        'apps': {
            "models": {
                "models": [
                    "aerich.models",
                    "apps.core.models",
                ],
                "default_connection": "default",
            },
        },
    }
    ```