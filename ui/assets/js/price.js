// query to return price of equipment for a given item
function getEquipmentPriceQuery(item_id) {
  return `SELECT SUM(price*quantity) AS total_equipment_price FROM Equipments \
		 			INNER JOIN ItemsEquipments \
					ON Equipments.equipment_id = ItemsEquipments.equipment_id \
					WHERE ItemsEquipments.item_id=${item_id}`;
}

// query to return price of materials for a given item
function getMaterialsPriceQuery(item_id) {
  return `SELECT SUM(price*quantity) AS total_material_price FROM Materials \
		 			INNER JOIN ItemsMaterials \
					ON Materials.material_id = ItemsMaterials.material_id \
					WHERE ItemsMaterials.item_id=${item_id}`;
}

// query to return price of workforce for a given item
function getWorkforcePriceQuery(item_id) {
  return `SELECT SUM(hourWage*quantity) AS total_workforce_price FROM WorkForces
					INNER JOIN ItemsWorkForces
					ON WorkForces.workForce_id = ItemsWorkForces.workForce_id
					WHERE ItemsWorkForces.item_id=${item_id}`;
}

async function getTotalEquipmentPrice(item_id) {
  return new Promise((resolve, reject) => {
    eel.dbGET(getEquipmentPriceQuery(item_id))((response) => {
      let response_p = JSON.parse(response)[0];
      if (
        response_p != undefined &&
        response_p["total_equipment_price"] != null
      ) {
        resolve(Number.parseFloat(response_p["total_equipment_price"]));
      } else {
        return resolve(0);
      }
    });
  });
}

async function getTotalMaterialsPrice(item_id){
	return new Promise((resolve, reject) => {
    eel.dbGET(getMaterialsPriceQuery(item_id))((response) => {
      let response_p = JSON.parse(response)[0];
      if (
        response_p != undefined &&
        response_p["total_material_price"] != null
      ) {
        resolve(Number.parseFloat(response_p["total_material_price"]));
      } else {
        return resolve(0);
      }
    });
  });
}

async function getTotalWorkforcePrice(item_id){
	return new Promise((resolve, reject) => {
    eel.dbGET(getWorkforcePriceQuery(item_id))((response) => {
      let response_p = JSON.parse(response)[0];
      if (
        response_p != undefined &&
        response_p["total_workforce_price"] != null
      ) {
        resolve(Number.parseFloat(response_p["total_workforce_price"]));
      } else {
        return resolve(0);
      }
    });
  });
}