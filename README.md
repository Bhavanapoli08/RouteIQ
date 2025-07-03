# RouteIQ – Journey Cost Prediction API 🚗💰

**RouteIQ** is a Flask-based REST API that predicts journey costs based on origin and destination inputs. It uses MongoDB to store route and historical cost data, and provides real-time estimates to users.

---

## 🚀 Features

- **Cost Prediction**: Calculates estimated cost for a given route using historical averages or custom logic.
- **Flask REST API**: Offers endpoints to predict costs and manage routes.
- **MongoDB Integration**: Stores route definitions and cost history for analytics and future improvements.
- **JSON Input/Output**: Clean request-response format.

---

## 🔧 Tech Stack

- **Backend**: Python 3.x, Flask
- **Database**: MongoDB
- **Data Modeling**: PyMongo for CRUD operations

---

Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Configure MongoDB:
Ensure MongoDB is running locally or remotely.

Set the connection string in config.py or via environment variable:
export MONGO_URI="mongodb://localhost:27017/routeiq"


## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Bhavanapoli08/RouteIQ.git
   cd RouteIQ

🚦 Usage
Start the API server:

flask run

| Method | Path            | Description                         | Body Example                                 |
| ------ | --------------- | ----------------------------------- | -------------------------------------------- |
| POST   | `/predict-cost` | Estimate cost between two locations | `{ "from": "A", "to": "B" }`                 |
| POST   | `/routes`       | Add a new route                     | `{ "from": "A", "to": "B", "distance": 10 }` |
| GET    | `/routes`       | List all routes                     | —                                            |
| GET    | `/history`      | Retrieve cost prediction history    | —                                            |


🎯 Sample Request

curl -X POST http://localhost:5000/predict-cost \
     -H "Content-Type: application/json" \
     -d '{ "from": "LocationA", "to": "LocationB" }'

     
Response:

{
  "from": "LocationA",
  "to": "LocationB",
  "estimated_cost": 125.40,
  "unit": "INR"
}

🧩 Architecture
Flask handles incoming requests and routes them to controllers.

Controllers interact with service layers to compute cost or manipulate data.

Services use PyMongo to read/write from routes and predictions collections in MongoDB.

Basic cost model: distance × rate_per_km or historical average.

✅ Notes
Create MongoDB collections: routes, predictions.

Extendable: Add features like surge pricing, time-based rates, or external distance APIs.

Add input validation, error handling, and authentication as needed.

🛠️ Future Improvements
Integrate real map APIs (e.g., Google Maps) for distance calculation.

User authentication & API key support.

Implement unit & integration tests.

Add Swagger/OpenAPI docs.
