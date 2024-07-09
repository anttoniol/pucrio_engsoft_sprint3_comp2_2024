from api.repositories.repository import Repository


class CoordinatesRepository(Repository):
    def save(self, data):
        cursor = self._db.cursor()
        query = "INSERT INTO coordinates (latitude, longitude, location_key) VALUES (%s, %s, %s)"
        values = (data["latitude"], data["longitude"], data["location_key"],)
        cursor.execute(query, values)

        self._db.commit()

        return {
            "row_id": cursor.lastrowid,
            "message": "Coordinates saved successfully!"
        }

    def get_by_coordinates(self, lat, lon):
        cursor = self._db.cursor()
        query = "SELECT * FROM coordinates WHERE latitude = %s AND longitude = %s"
        values = (lat, lon,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is not None:
            return {
                "id": result[0],
                "latitude": result[1],
                "longitude": result[2],
                "location_key": result[3]
            }

        return None

    def save_if_not_exists(self, data):
        query_result = self.get_by_coordinates(data["latitude"], data['longitude'])

        if query_result is None:
            coordinates_data = {
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "location_key": data["location_key"]
            }
            insert_result = self.save(coordinates_data)
            return insert_result

        return {
            "row_id": query_result["id"],
            "message": "Coordinates obtained successfully!"
        }
