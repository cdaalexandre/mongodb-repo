from models.user import create_user, list_users, update_user, delete_user

if __name__ == "__main__":
    print("=== CRUD com MongoDB ===")

    # CREATE
    uid = create_user("Alexandre", "alexandre@example.com")
    print(f"Usuário criado com ID: {uid}")

    # READ
    print("Lista de usuários:", list_users())

    # UPDATE
    update_count = update_user("Alexandre", "novoemail@example.com")
    print(f"Usuários atualizados: {update_count}")

    # DELETE
    delete_count = delete_user("Alexandre")
    print(f"Usuários deletados: {delete_count}") 
