package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
)

func getRoot(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Printf("Could not read body: %s\n", err)
	}
	fmt.Printf("Request body: %s\n", body)
	io.WriteString(w, "Got it!")
}

func main() {
	fmt.Println("Starting to listen...")
	http.HandleFunc("/", getRoot)
	http.ListenAndServe(":8000", nil)
}
