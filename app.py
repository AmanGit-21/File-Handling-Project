import streamlit as st
from pathlib import Path

st.set_page_config(page_title="File Manager", page_icon="📁", layout="centered")

st.title("📁 File Handling Manager")
st.caption("Create, Read, Update, and Delete text files — built with Streamlit")

# Sidebar menu (this replaces your old print()+input() menu)
menu = st.sidebar.radio(
    "Choose an operation",
    ["Create", "Read", "Update", "Delete"]
)

# ---------------- CREATE ----------------
if menu == "Create":
    st.header("📝 Create a File")
    name = st.text_input("File name (e.g. notes.txt)")
    data = st.text_area("What do you want to write?")

    if st.button("Create File"):
        if not name:
            st.warning("Please enter a file name.")
        else:
            path = Path(name)
            try:
                if not path.exists():
                    with open(path, "w") as fs:
                        fs.write(data)
                    st.success("✅ File created successfully!")
                else:
                    st.error("⚠️ File name already exists.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ---------------- READ ----------------
elif menu == "Read":
    st.header("📖 Read a File")
    name = st.text_input("File name to read")

    if st.button("Read File"):
        if not name:
            st.warning("Please enter a file name.")
        else:
            path = Path(name)
            try:
                if path.exists():
                    with open(path, "r") as fs:
                        content = fs.read()
                    st.success("File content:")
                    st.code(content)
                else:
                    st.error("⚠️ No such file exists.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ---------------- UPDATE ----------------
elif menu == "Update":
    st.header("✏️ Update a File")
    name = st.text_input("File name to update")
    operation = st.radio("Choose an operation", ["Rename", "Append content", "Overwrite"])

    path = Path(name) if name else None

    if operation == "Rename":
        new_name = st.text_input("New file name")
        if st.button("Rename File"):
            if not name or not new_name:
                st.warning("Please fill in both file names.")
            elif not path.exists():
                st.error("⚠️ Original file does not exist.")
            else:
                new_path = Path(new_name)
                if new_path.exists():
                    st.error("⚠️ A file with the new name already exists.")
                else:
                    path.rename(new_path)
                    st.success("✅ Renamed successfully!")

    elif operation == "Append content":
        data = st.text_area("What do you want to append?")
        if st.button("Append"):
            if not name:
                st.warning("Please enter a file name.")
            elif not path.exists():
                st.error("⚠️ No such file exists.")
            else:
                with open(path, "a") as fs:
                    fs.write("\n" + data)
                st.success("✅ Appended successfully!")

    elif operation == "Overwrite":
        data = st.text_area("What do you want to overwrite with?")
        if st.button("Overwrite"):
            if not name:
                st.warning("Please enter a file name.")
            elif not path.exists():
                st.error("⚠️ No such file exists.")
            else:
                with open(path, "w") as fs:
                    fs.write(data)
                st.success("✅ Overwritten successfully!")

# ---------------- DELETE ----------------
elif menu == "Delete":
    st.header("🗑️ Delete a File")
    name = st.text_input("File name to delete")

    if st.button("Delete File", type="primary"):
        if not name:
            st.warning("Please enter a file name.")
        else:
            path = Path(name)
            try:
                if path.exists():
                    path.unlink()
                    st.success("✅ File deleted successfully!")
                else:
                    st.error("⚠️ No such file exists.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

st.divider()
st.caption("Tip: files are created in the same folder where you run this app (`streamlit run file_manager_app.py`).")
