from app.supabase_client import supabase


def fetch_data_from_table(table_name):
    try:
        response = supabase.table(table_name).select('*').execute()

        if hasattr(response, 'error') and response.error:
            return {"message": "Error fetching data", "error": str(response.error)}, 500

        if hasattr(response, 'data') and response.data:
            return {"message": "OK", "data": response.data}, 200

        return {"message": "No data found", "error": "Data is empty"}, 404

    except Exception as e:
        return {"message": "Internal server error", "error": str(e)}, 500
