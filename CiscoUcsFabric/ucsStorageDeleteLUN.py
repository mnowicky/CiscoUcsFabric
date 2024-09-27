def delete_lun(session, base_url, lun_name):
    url = f"{base_url}/storage/lun/{lun_name}"

    response = session.delete(url)
    if response.status_code == 204:
        print(f"LUN '{lun_name}' deleted successfully.")
    else:
        print("Failed to delete LUN:", response.content)

delete_lun(session, base_url, "LUN-Example")

