package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func part2(l1, l2 []int) int {
	r := 0
	m := make(map[int]int)
	for _, v := range l1 {
		m[v] += 1
	}

	for _, v := range l2 {
		r += m[v] * v
	}

	return r
}

func main() {
	list1, list2 := []int{}, []int{}
	var result int

	f, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}

	defer f.Close()

	r := bufio.NewReader(f)

	for {
		line, _, err := r.ReadLine()
		if len(line) > 0 {
			v := strings.Fields(string(line))
			int1, err := strconv.Atoi(v[0])
			if err != nil {
				panic(err)
			}
			int2, err := strconv.Atoi(v[1])
			if err != nil {
				panic(err)
			}

			list1 = append(list1, int1)
			list2 = append(list2, int2)
		}
		if err != nil {
			break
		}
	}

	slices.Sort(list1)
	slices.Sort(list2)

	for i := 0; i < 1000; i++ {
		if list1[i] > list2[i] {
			result += list1[i] - list2[i]
		} else {
			result += list2[i] - list1[i]
		}
	}

	fmt.Println(result)

	fmt.Println(part2(list1, list2))
}
