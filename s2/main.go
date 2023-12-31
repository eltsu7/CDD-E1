package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
)

func getRoot(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		fmt.Printf("Could not read body: %s\n", err)
	}
	fmt.Printf("Request body: %s\n", body)
	io.WriteString(w, "Got it!")

	_ = os.Mkdir("logs", os.ModePerm)

	file, err := os.OpenFile("logs/service2.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	_, err = file.Write(append(body, byte('\n')))
	if err != nil {
		panic(err)
	}

	err = file.Close()
	if err != nil {
		panic(err)
	}
}

func main() {
	fmt.Println("Starting to listen...")
	http.HandleFunc("/", getRoot)
	http.ListenAndServe(":8000", nil)
}
