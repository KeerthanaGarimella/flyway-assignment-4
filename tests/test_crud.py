import unittest
import mysql.connector

class TestSubscribers(unittest.TestCase):
    def setUp(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="subscribers"
        )
        self.cursor = self.conn.cursor()

    def test_create(self):
        self.cursor.execute("INSERT INTO subscriber (name, email) VALUES ('John', 'john@example.com')")
        self.conn.commit()

    def test_read(self):
        self.cursor.execute("SELECT * FROM subscriber")
        rows = self.cursor.fetchall()
        self.assertGreater(len(rows), 0)

    def test_update(self):
        self.cursor.execute("UPDATE subscriber SET name='Jane' WHERE email='john@example.com'")
        self.conn.commit()

    def test_delete(self):
        self.cursor.execute("DELETE FROM subscriber WHERE email='john@example.com'")
        self.conn.commit()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    unittest.main()
