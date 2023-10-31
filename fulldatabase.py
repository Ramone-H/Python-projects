import mysql.connector


# we will connect or reset connection to my sql to mysql server using the mysql connnector

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456")
    return connection


my_connection = connect()


# We can create function that will show all databases available on the server
def show_databases():
    my_cursor = my_connection.cursor()
    my_cursor.execute("SHOW DATABASES")
    for row in my_cursor.fetchall():
        print(row[0])
        # we can store these in a list and use it to check if a database exists


# We will create a function that will create a database

def create_database(name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"CREATE DATABASE {name}")


# We will create a function that will use a database, This will overide the original connection

def use_database(db_name):
    try:
        my_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database=f"{db_name}")
        if my_connection.is_connected():
            cursor = my_connection.cursor()
            cursor.execute("select database();")  # This line of code is used to get the database name
            record = cursor.fetchone()
            print("You're connected to database: ", record[0])
            return my_connection
    except:
        print("Database does not exist!")


def delete_database(db_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"DROP DATABASE {db_name}")


def show_tables():
    my_cursor = my_connection.cursor()
    my_cursor.execute("SHOW TABLES")
    for rows in my_cursor.fetchall():
        print(rows[0])


def create_table(table_name):
    my_cursor = my_connection.cursor()
    # when creating a table, at least one(1) column must be done
    my_cursor.execute(f"CREATE TABLE {table_name}(def VARCHAR(100))")


def delete_table(table_name):
    try:
        my_cursor = my_connection.cursor()
        my_cursor.execute(f"DROP TABLE {table_name}")
    except:
        print("Table does not exist")


def add_column(table, name_list, type_list):
    my_cursor = my_connection.cursor()
    sql_command = f"ALTER TABLE {table} ADD COLUMN ("
    n_length = len(name_list)
    for i in range(n_length):
        sql_command += name_list[i] + " " + type_list[i]
        if i < n_length - 1:
            # this should append a comma after each column in the table up to the last
            sql_command += ", "
    else:
        sql_command += ")"

    my_cursor.execute(sql_command)
    my_connection.commit()


def remove_column(table_name, column_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {column_name}")
    my_connection.commit()
    print(f"{column_name} was deleted!")


def remove_def_column(table_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN def")
    my_connection.commit()
    print("Default column was deleted")


def show_all_column(table_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"Describe {table_name}")
    description = my_cursor.fetchall()
    for row in description:
        print(row)


def show_table_column(table_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"Describe {table_name}")
    description = my_cursor.fetchall()
    column_list = []
    for row in description:
        print(row)
        # this will create a list of all the columns in a specific table
        column_list.append(row[0])
    return column_list

# This function is used to update a table
def update_table(table_name):
    try:
        my_cursor = my_connection.cursor()
        condition_set = input("What would you like to set?")
        condition_where = input("Set the where condition:")
        my_cursor.execute(f"UPDATE {table_name} SET {condition_set} WHERE {condition_where}")
        my_connection.commit()
    except:
        print("Something went wrong, retry the conditions")
def select_all_query(table_name):
    my_cursor = my_connection.cursor()
    my_cursor.execute(f"SELECT * FROM {table_name}")
    records = my_cursor.fetchall()
    for rows in records:
        print(rows)


def insert_values(table, column, values):
    my_cursor = my_connection.cursor()
    placeholder = "%s"
    placeholder_i = "%s"
    c_length = len(column)
    for i in range(c_length - 1):
        placeholder = placeholder + ", " + placeholder_i

    sqlcommand = f"INSERT INTO {table} VALUES ({placeholder})"
    # one record at a time can be entered
    my_cursor.execute(sqlcommand, values)
    my_connection.commit()


# this function goes with insert function to get the values to place inside the columns
def get_values_for_table(column_list):
    col_length = len(column_list)
    value_list = []
    for i in range(col_length):
        item = input(f"Enter the {column_list[i]}: ")
        value_list.append(item)
    # convert to a tuple since the execution command only accepts tuple
    values = tuple(value_list)
    return values


# this function is used to get a name from the user
def collect_name():
    name1 = input("Enter a name: ")
    return name1


def create_table_columns():
    columns = []
    data_type = []
    ini = 0
    print("You can press x to stop adding columns")
    # This loop is used to add the column names
    while ini == 0:
        c_name = input("Add a column name: ")
        if c_name == 'x':
            break
        check = input("Are you sure, y- yes or n - no")
        if check == "y":
            columns.append(c_name)
        else:
            print("Add another column")
    else:
        print("column list complete")

    c_length = len(columns)
    # This for loop specify the data type for each column in the table
    for i in range(c_length):
        print("DATA TYPES:\n1:INT\n2:VARCHAR(100)")
        choice = int(input(f"What is the data type of{columns[i]}: "))
        if choice == 1:
            data_type.append("INT")
        elif choice == 2:
            data_type.append("VARCHAR(100)")
        else:
            print("invalid")
            data_type.append("VARCHAR(250)")
    return columns, data_type


# getting an input from user to choose what to do

enter = 0
while input != 5:
    my_connection = connect()
    print("Choose 1: To create a new database")
    print("Choose 2: To show all databases")
    print("Choose 3: To delete a database")
    print("Choose 4: To use a database")
    print("Choose 5: To exit")
    try:

        enter = int(input("Which do you Select? "))
        if enter == 1:
            print("You may now choose a name for your new database!")
            name = collect_name()
            create_database(name)
        elif enter == 2:
            print("Here is a list of all the databases")
            show_databases()
        elif enter == 3:
            print("Which database would you like to delete?")
            db_name = collect_name()
            delete_database(db_name)
        elif enter == 4:
            print("Which database would you like to use?")
            user_database = collect_name()
            my_connection = use_database(user_database)
            choose = 0
            while choose != 8:
                print("Choose 1: To show all tables")
                print("Choose 2: To create a table")
                print("Choose 3: To alter a table")
                print("Choose 4: To insert values in a table")
                print("Choose 5: To update a table")
                print("Choose 6: To delete a table")
                print("Choose 7: To show all values in a table")
                print("Choose 8: To exit")
                choose = int(input("What would you like to do? "))
                if choose == 1:
                    show_tables()
                elif choose == 2:
                    print("You may now choose a name for your new table!")
                    table_name2 = collect_name()
                    create_table(table_name2)
                elif choose == 3:
                    print("which table would you like to alter? ")
                    altered_table = collect_name()
                    print(
                        "Choose 'a' to Add a column\nChoose 'b' to Drop a column\nchoose 'c' to remove default column"
                        "\nchoose 'd' to show all column")
                    option = input("What do you choose? ")
                    if option == "a":
                        columnA, datatypeA = create_table_columns()
                        add_column(altered_table, columnA, datatypeA)
                    elif option == "b":
                        print("Enter the column name you would like to remove")
                        column_name = collect_name()
                        remove_column(altered_table, column_name)
                    elif option == "c":
                        remove_def_column(altered_table)
                    elif option == "d":
                        show_all_column(altered_table)
                    else:
                        print("Invalid input!!!")
                elif choose == 4:
                    print("Which table would you like to insert a record into")
                    i_table = collect_name()
                    print("Here is a list of all the columns inside this table!")
                    all_column = show_table_column(i_table)
                    all_values = get_values_for_table(all_column)
                    insert_values(i_table, all_column, all_values)
                elif choose == 5:
                    print("You may now choose the table you want to update!")
                    table_name_5 = collect_name()
                    update_table(table_name_5)

                elif choose == 6:
                    print("You may now choose the table you want to delete!")
                    table_name_6 = collect_name()
                    delete_table(table_name_6)
                elif choose == 7:
                    print("You may now choose the table you want to query!")
                    table_name_7 = collect_name()
                    select_all_query(table_name_7)
                elif choose == 8:
                    break
                else:
                    print("Invalid input")

        elif enter == 5:
            break
        else:
            print("Invalid value entered!")
    except:
        print("An error occured")
