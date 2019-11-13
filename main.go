package main

import (
    "encoding/json"
    "github.com/gorilla/mux"
    "log"
    "net/http"
)

// The person Type
type Person struct {
    ID        string   `json:"id,omitempty"`
    Firstname string   `json:"firstname,omitempty"`
    Lastname  string   `json:"lastname,omitempty"`
    Address   *Address `json:"address,omitempty"`
}
type Address struct {
    City  string `json:"city,omitempty"`
    State string `json:"state,omitempty"`
}

var people []Person

//Default
func Default(w http.ResponseWriter, r *http.Request) {

    json.NewEncoder(w).Encode("Welcome to the IoT Bootcamp 2019!")

    return

}

// Display all from the people var
func GetPeople(w http.ResponseWriter, r *http.Request) {
    json.NewEncoder(w).Encode(people)
}

// Display a single data
func GetPerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    for _, item := range people {
        if item.ID == params["id"] {
            json.NewEncoder(w).Encode(item)
            return
        }
    }
    json.NewEncoder(w).Encode(&Person{})
}

// create a new person
func CreatePerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    var person Person
    _ = json.NewDecoder(r.Body).Decode(&person)
    person.ID = params["id"]
    people = append(people, person)
    json.NewEncoder(w).Encode(people)
}

// Delete a person
func DeletePerson(w http.ResponseWriter, r *http.Request) {
    params := mux.Vars(r)
    for index, item := range people {
        if item.ID == params["id"] {
            people = append(people[:index], people[index+1:]...)
            break
        }
        json.NewEncoder(w).Encode(people)
    }
}

// main function to boot up everything
func main() {
    router := mux.NewRouter()
    people = append(people, Person{ID: "1", Firstname: "Leonard", Lastname: "Michalas", Address: &Address{City: "Frankfurt am Main", State: "Hessen"}})
    people = append(people, Person{ID: "2", Firstname: "Markus", Lastname: "Stulle", Address: &Address{City: "München", State: "Bayern"}})
    people = append(people, Person{ID: "3", Firstname: "Dejan", Lastname: "Boberic", Address: &Address{City: "Düsseldorf", State: "NRW"}})
    router.HandleFunc("/", Default).Methods("GET")
    router.HandleFunc("/people", GetPeople).Methods("GET")
    router.HandleFunc("/people/{id}", GetPerson).Methods("GET")
    router.HandleFunc("/people/{id}", CreatePerson).Methods("POST")
    router.HandleFunc("/people/{id}", DeletePerson).Methods("DELETE")
    log.Fatal(http.ListenAndServe(":8080", router))
}
