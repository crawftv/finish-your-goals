from models import DB, Task

t1 = Task(
        name="t1",
        monday=True,
        tuesday=True,
        wednesday=True,
        thursday=True,
        friday=True,
        saturday=True,
        sunday=True,
        start_time=0,
        end_time=45,
        interval=15,
        user_id='auth0|5de6e9817c6c9c0ed3e6d8f5'
        )
DB.session.add(t1)
DB.session.commit()
