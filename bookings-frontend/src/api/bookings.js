export const API_URL = "http://127.0.0.1:8000/api/";

export const getRooms = async () => {
  const response = await fetch(API_URL + "rooms/all/");
  return response.json();
};

export const getSeats = async () => {
  const response = await fetch(API_URL + "seats/all/");
  return response.json();
};

export const getCars = async () => {
  const response = await fetch(API_URL + "cars/all/");
  return response.json();
};
