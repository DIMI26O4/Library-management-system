import streamlit as st
import pandas as pd
import os

#Function for category of books. will be called in Admin and user home page both.
def show_categories():
    file = "category_of_books.csv"

    if os.path.exists(file):
        df = pd.read_csv(file)
        st.subheader("Product Details")
        st.dataframe(df, use_container_width=True)


st.title("Library Management System")
st.write("Welcome to the Library App!")

# 2 types of users 
# admin is the role. user id and password is 'adm' 
users = {
    "adm": {"password": "adm", "role": "admin"},
    "user": {"password": "user", "role": "user"}
}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None


if not st.session_state.logged_in:
    
    st.subheader("Login")

    username = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
            if username in users and users[username]["password"] == password:
                st.session_state.logged_in = True
                st.session_state.role = users[username]["role"]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with col2:
        if st.button("Cancel"):
            st.rerun()

else:

    st.sidebar.write(f"Logged in as **{st.session_state.role}**")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # Role-based navigation in the system through a menu choice
    # Admin can navigate membership, Transactions and reports module
    # User can navigate transactions and reports module only
    if st.session_state.role == "admin":
        menu = ["Admin Home", "Maintenance", "Transactions", "Reports"]
    else:
        menu = ["User Home", "Transactions", "Reports"]

    choice = st.sidebar.selectbox("Navigation", menu)

    # Admin Pages
    if choice == "Admin Home":
        st.header("Home Page")
        st.write("Welcome Admin!")
        show_categories()

    elif choice == "Maintenance":
        st.header("Membership Management")
        maintenance_menu = st.selectbox(
        "Select Function",
        [
            "Add Membership",
            "Update Membership",
            "Add Book/Movie",
            "Update Book/Movie",
            "Add User",
            "Update User"
        ]
        )

        
        
        if maintenance_menu == "Add Membership":
            st.subheader("Add Membership")
            file = "members.csv"

            
            if os.path.exists(file):
                df = pd.read_csv(file)
            else:
                df = pd.DataFrame(columns=[
                "Member_ID",
                "First_Name",
                "Last_Name",
                "Contact_Name",
                "Address",
                "Aadhar",
                "Start_Date",
                "End_Date",
                "Membership_Type"
                ])

            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            contact_name = st.text_input("Contact Name")
            address = st.text_input("Contact Address")
            aadhar = st.text_input("Aadhar Card No")

            start_date = st.date_input("Start Date")
            end_date = st.date_input("End Date")

            membership = st.radio(
                "Membership",
                ["Six Months", "One Year", "Two Years"]
                )

            col1, col2 = st.columns(2)

            # Cancel
            with col1:
                if st.button("Cancel"):
                    st.rerun()

            # Confirm
            with col2:
                if st.button("Confirm"):
                    if first_name == "" or aadhar == "":
                        st.error("Please fill required fields")
                    else:
                        new_member = {
                            "Member_ID": f"MBR{len(df)+1}",
                            "First_Name": first_name,
                            "Last_Name": last_name,
                            "Contact_Name": contact_name,
                            "Address": address,
                            "Aadhar": aadhar,
                            "Start_Date": start_date,
                            "End_Date": end_date,
                            "Membership_Type": membership
                        }

                        df = pd.concat([df, pd.DataFrame([new_member])], ignore_index=True)
                        df.to_csv(file, index=False)

                        st.success("Membership added successfully")
              

            

            
        
        
        
        
        elif maintenance_menu == "Update Membership":
            st.subheader("Update Membership")





        # Add Book/movie
        elif maintenance_menu == "Add Book/Movie":
            st.subheader("Add Book/Movie")
            file = "books.csv"

            if os.path.exists(file):
                df = pd.read_csv(file)
            else:
                df = pd.DataFrame(columns=[
                "Item_ID",
                "Type (Book/Movie)",
                "Title",
                "Procurement_Date",
                "Quantity",
                "Available"
                ])

            # Radio Button
            item_type = st.radio(
                "Select Type",
                ["Book", "Movie"],
                horizontal=True
            )

            # Text box
            title = st.text_input("Book/Movie Name")

            # Calendar
            procurement_date = st.date_input("Date of Procurement")

            # Quantity default = 1
            quantity = st.number_input(
                "Quantity/Copies",
                min_value=1,
                value=1,
                step=1
            )

            col1, col2 = st.columns(2)

            # Cancel button
            with col1:
                if st.button("Cancel"):
                    st.rerun()

            # Confirm button
            with col2:
                if st.button("Confirm"):

                    if title == "":
                        st.error("Please enter Book/Movie name")

                    else:
                        new_row = {
                            "Item_ID": f"ITM{len(df)+1}",
                            "Type (Book/Movie)": item_type,
                            "Title": title,
                            "Procurement_Date": procurement_date,
                            "Quantity": quantity,
                            "Available": True
                        }

                        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                        df.to_csv(file, index=False)

                        st.success("Added successfully")






        elif maintenance_menu == "Update Book/Movie":
            st.subheader("Update Book/Movie")


        elif maintenance_menu == "Add User":
            st.subheader("Add User")

            file = "users.csv"

            if os.path.exists(file):
                df = pd.read_csv(file)
            else:
                df = pd.DataFrame(columns=[
                    "Username",
                    "Password",
                ])

            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Cancel"):
                    st.rerun()

            with col2:
                if st.button("Confirm"):

                    if username == "" or password == "":
                        st.error("Username and Password required")

                    else:
                        new_user = {
                            "Username": username,
                            "Password": password,  
                        }

                        df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
                        df.to_csv(file, index=False)

                        st.success("User added successfully")



        elif maintenance_menu == "Update User":
            st.subheader("Update User")

    
    
    elif choice == "Transactions":
        st.header("Transactions Module")
        
        transaction_menu = st.selectbox(
        "Select Function",
        ["Issue Book", "Return Book"]
        )
        
        
    elif choice == "Reports":
        st.header("Reports Module")
    
    #User Pages
    elif choice == "User Home":
        st.header("User Home Page")
        st.write("Welcome User!")
        show_categories()

