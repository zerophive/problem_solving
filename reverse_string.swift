#!/usr/bin/env swift

/*
Everyone does one of these, I just wanted to try one in
swift without using the built-in reversed() method
*/

func myReverseString(_ string: String) -> String {
    var strIt = string.makeIterator()
    var newCharArray: [Character] = []
    var char: Character?

    char = strIt.next()
    repeat {
        newCharArray.insert(char!, at: 0)
        char = strIt.next()
    } while char != nil

    let newString = newCharArray.map {$0.description}.joined()

    return newString
}

if CommandLine.argc > 1 {
	let string = myReverseString(CommandLine.arguments[1])
    print(string)
} else {
    print("No string to reverse has been entered!")
}
