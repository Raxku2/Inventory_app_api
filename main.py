from pydantic import BaseModel


class itemData(BaseModel):
    item_id: int
    item_name: str = ""
    item_description: str = ""
    item_quantity: int
    item_price: int


from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse


app = FastAPI()


@app.get("/")
def home():
    return RedirectResponse("/docs")


inventory: list = []


@app.post("/insert")
def insert(item: itemData):
    item_name = item.item_name.strip()
    item_description = item.item_description.strip() or None
    item_quantity = item.item_quantity
    item_price = item.item_price
    item_id = item.item_id

    if (
    item_name is None or item_name.strip() == "" or
    item_description is None or item_description.strip() == "" or
    item_quantity is None or
    item_price is None or
    item_id is None
    ):
        return JSONResponse({'message': "invalid"})


    inventory.append(
        {
            "_id": item_id,
            "name": item_name,
            "desc": item_description,
            "quantity": item_quantity,
            "price": item_price,
        }
    )
    return JSONResponse(
        {"message": "item added sucessfully", "data": inventory}, status_code=200
    )


@app.get("/inventory")
def showInventory():
    if len(inventory):
        return JSONResponse(status_code=200, content={"data": inventory})
    else:
        return JSONResponse(
            status_code=400, content={"message": "inventory is empty now"}
        )


@app.get("/item/{item_id}")
def showOneItem(item_id: int):
    data = ""
    if type(item_id) == int and item_id:
        data = [item for item in inventory if item["_id"] == item_id]

    if data:
        return JSONResponse({"data":data})
    else:
        return JSONResponse(
            status_code=400, content={"message": "Item not found"}
        )


@app.put("/item/{edit_item_id}")
def editOneItem(edit_item_id: int, item: itemData):

    # Validate ID
    if not isinstance(edit_item_id, int) or edit_item_id <= 0:
        return JSONResponse(status_code=400, content={"message": "Invalid ID"})

    # Search for existing item
    found_index = None
    existing_item = None

    for index, it in enumerate(inventory):
        if it["_id"] == edit_item_id:
            found_index = index
            existing_item = it
            break

    # If not found
    if existing_item is None:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

    # Extract old values
    old_name = existing_item.get("name")
    old_desc = existing_item.get("desc")
    old_quantity = existing_item.get("quantity")
    old_price = existing_item.get("price")

    # New incoming values
    new_name = item.item_name.strip()
    new_desc = item.item_description.strip() or None
    new_quantity = item.item_quantity
    new_price = item.item_price

    # Build updated document
    newDoc = {
        "_id": edit_item_id,
        "name": new_name if new_name else old_name,
        "desc": new_desc if new_desc else old_desc,
        "quantity": new_quantity if new_quantity is not None else old_quantity,
        "price": new_price if new_price is not None else old_price,
    }

    # Save update
    inventory[found_index] = newDoc

    return JSONResponse({"data": inventory})

@app.delete("/item/{item_id}")
def deleteItem(item_id:int):

    for index, it in enumerate(inventory):
        if it["_id"] == item_id:
            deleted_item = inventory.pop(index)   # <— delete
            return {"message": "deleted", "item": deleted_item}

    return JSONResponse(status_code=404, content={"message": "Item not found"})