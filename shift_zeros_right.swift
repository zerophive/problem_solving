#!/usr/bin/env swift

import Darwin

/*
given an array, shift all zeros to the right side
*/


let array = [1,0,0,2,5,0]
print(array)

// This one works only for natural numbers
// for all Integers, this does not work
func shiftZerosRightCheapo(_ array: [Int]) -> [Int] {
	var array = array
	array.sort() {$0 > $1}

	return array
}

print(shiftZerosRightCheapo(array))

/*
actually the real question was to do this inplace, beacuse I guess
the compiler isn't going to optimize this down enough for us?? Nenyways,
this is a type of interview question out there, sooooooo.....
*/

var array2 = [-1,0,0,2,5,0,15,2,0,4,0,3,45]
print(array2)

/*
this one works, but it does shift the order around as a result.
Though I also think this is probably more efficient as the array
is ONLY walked through once, I think
*/
func shiftZerosRightOk(_ array: inout [Int]) {

	func getLastNoneZeroIndex(_ index: Int) -> Int {
		var index = index
		while array[index] == 0 {
			index -= 1
		}
		return index
	}

	var lastIndex = array.count - 1
	lastIndex = getLastNoneZeroIndex(lastIndex)

//	for (index,item) in array.enumerated() {
	for index in 1...array.count - 1 {
		if index >= lastIndex  { break }
		if array[index] == 0 {
			array.swapAt(index, lastIndex)
			lastIndex -= 1
			lastIndex = getLastNoneZeroIndex(lastIndex)
		}
	}
}

shiftZerosRightOk(&array2)
print(array2)

/*
this one is more correct, it moves the zeros to the right
but does not alter the order of the elements otherwise
don't like the array out of bounds checks, but meh
That said, this also isn't really "one pass" either
*/

func shiftZerosRightFauxPass(_ array: inout [Int]) {
	let maxIndex = array.count - 1

	func getNexttNoneZeroIndex(_ index: Int) -> Int {
		if index == maxIndex { return index }
		var index = index + 1
		while array[index] == 0 {
			if index == maxIndex { return index }
			index += 1
		}
		return index
	}


	for index in 1...maxIndex {
		if array[index] == 0 {
			let swapIndex = getNexttNoneZeroIndex(index)
			array.swapAt(index, swapIndex)
		}
	}
}

/*
I saw this cool idea somewhere, but I would have to rework a lot of
shiftZeroRightFauxPass to make use it, so bah
*/
extension Array {
	subscript(safe index: Index) -> Element? {
		let isValidIndex = index >= 0 && index < count
		return isValidIndex ? self[index] : nil
	}
}

var array3 = [-1,0,0,2,5,0,15,2,0,4,0,3,45]

shiftZerosRightFauxPass(&array3)
print(array3)


/* 
This is a one pass solution that is correct
after thinking about it I was on the right idea, but needed to
rethink how I went about scanning the array and how I used marker
indices
*/
func shiftZerosRight(_ array: inout [Int]) {
	let maxIndex = array.count - 1

    var index = 0
    for swapIndex in 0...maxIndex {
        if array[swapIndex] != 0 {
            array.swapAt(index, swapIndex)
            index += 1
        }
    }
}

var array4 = [-1,0,0,2,5,0,15,2,0,4,0,3,45]

shiftZerosRight(&array4)
print(array4)
