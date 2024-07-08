package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var a, b, c int
	fmt.Fscan(reader, &a, &b, &c)

	fmt.Fprintln(writer, getMiddleElement(a, b, c))
}

func getMiddleElement(a, b, c int) int {
	if a > b && b > c {
		return b
	} else if a > c && c > b {
		return c
	} else {
		return a
	}
}
