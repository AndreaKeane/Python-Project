import pytest
import os, time
import main
import database


@pytest.fixture(scope="module", autouse = True)
def configuration():
    dbname = 'test_app_' + str(int(time.time()))
    os.environ['MONGO_DB_NAME'] = dbname

    yield

    database.mongo_client().drop_database(dbname)


# def test_do_stuff(): 
#     response = main.do_stuff("Testing from test module")
#     assert response