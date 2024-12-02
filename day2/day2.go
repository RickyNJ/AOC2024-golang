package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func main() {
	result := 0
	f, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	defer f.Close()
	r := bufio.NewReader(f)
	for {
		line, _, err := r.ReadLine()
		if err != nil {
			if err == io.EOF {
				break
			}
			panic(err)
		}

		measurements := strings.Fields(string(line))
		intslice := []int{}
		for _, v := range measurements {
			iv, err := strconv.Atoi(v)
			if err != nil {
				panic(err)
			}
			intslice = append(intslice, iv)
		}

		if intslice[0] < intslice[len(intslice)-1] {
			if checksafetyPositive(intslice, true) {
				result++
			}
		} else if intslice[0] > intslice[len(intslice)-1] {
			if checksafetyNegative(intslice, true) {
				result++
			}
		}
	}
	fmt.Println(result)
}

func checksafetyPositive(sl []int, firstpass bool) bool {
	for i := 1; i < len(sl); i++ {
		diff := sl[i] - sl[i-1]
		if diff <= 0 || diff > 3 {
			if firstpass {
				newslice := append(sl[:i], sl[i+1:]...)
				return checksafetyPositive(newslice, false)
			}
			return false
		}
	}
	return true
}

func checksafetyNegative(sl []int, firstpass bool) bool {
	for i := 1; i < len(sl); i++ {
		diff := sl[i] - sl[i-1]
		if diff >= 0 || diff < -3 {
			if firstpass {
				newslice := append(sl[:i], sl[i+1:]...)
				return checksafetyPositive(newslice, false)
			}
			return false
		}
	}
	return true
}
