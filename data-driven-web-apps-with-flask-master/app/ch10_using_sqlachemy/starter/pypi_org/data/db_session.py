import sqlalchemy as sa
import sqlalchemy.orm as orm

from pypi_org.data.modelbase import SqlAlchemyBase

factory = None


def global_init(db_file: str):
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception('You must specify a db file.')

    conn_str = 'sqlite:///' + db_file.strip()
    print('Connecting to DB with {}'.format(conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str, echo=False, connect_args={'check_same_thread': False})
    factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import pypi_org.data.__all_models

    SqlAlchemyBase.metadata.create_all(engine)
