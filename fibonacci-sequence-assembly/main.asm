; TWF - Last Modified: 24 September 2011
; ------------------------------------------------------------
; This program calculates numbers of the Fibonacci series.
; It asks the user for the number of numbers to display and
; Then outputs its calculations.
; ------------------------------------------------------------

.model small
.stack ; Stack memory space for program instructions

.data

	; Some messages to the user
	question DB "Enter how many Fibonacci numbers must be displayed: $"
	newline DB 10, 13, "$"

.code
	
	; Skip variable declaration
	jmp start

	; Define some variables
	max DB "0"
	tmp DB 0
	sum DB 0
	a DB 0
	b DB 1
	i DB "0"
	j DB 0
	
	start:
	
		; Put the address of data into ax, ds
		mov ax, @data 
		mov ds, ax
	
		; Skip inputerror
		jmp ask
	
	inputerror:
	
		; Newline and return
		mov ah, 09
		mov dx, offset newline
		int 21h
	
	ask:
	
		; Ask the question
		mov ah, 09
		mov dx, offset question
		int 21h
		
		; Use subfunction one to get first number from keyboard
		mov ah, 01
		int 21h
		mov max, al
		
		; Test for correct input
		cmp max, "1"
		ja inputerror
		cmp max, "0"
		jb inputerror
		
		; Test for two digit number
		cmp max, "1"
		je twodigit
		
		; Get second digit - we no longer care about the first digit
		mov ah, 01
		int 21h
		mov max, al
		
		; Test for correct input
		cmp max, "3"
		jb inputerror
		
		; Jump to calculation procedure
		jmp calc
		
	twodigit:
		
		; Multiply the first digit by ten
		mov al, j
		cmp al, 10
		je next
		inc j
		add al, al
		jmp twodigit
		
	next:
		
		; Reset j and save tmp
		mov j, 0
		mov tmp, al
	
		; Get the second digit
		mov ah, 01
		int 21h
		
		; Test for correct input
		cmp al, "4"
		ja inputerror
		
		; Add the second digit to the first
		add al, tmp
		mov max, al
		
	calc:

		; Check to see if we have looped enough times
		mov al, i
		cmp al, max
		je exexit
		inc i
	
		; Newline and return
		mov ah, 09
		mov dx, offset newline
		int 21h

		; Check to see if sum is more than one digit
		cmp sum, 9
		ja two
	
		; Display the sum
		mov ah, 02
		mov dl, sum
		add dl, 48
		int 21h
	
	return:
			
		; Assign a and b to the next in the series
		mov al, b
		mov a, al
		mov al, sum
		mov b, al
						
		; Sum the previous two numbers
		mov al, a
		mov sum, al
		mov al, b
		add sum, al
		
			; Start the cycle again
			jmp calc
	
	exexit:
	
		; To avoid Relative jump out of range error
		jmp exit
		
	two:
	
		; Check to see if sum is more than two digits
		cmp sum, 99
		ja three

		; We must reset j and tmp before subtra is called
		mov j, 0
		mov al, sum
		mov tmp, al
		
	subtra:
	
		; Divide the number by 10 in order to split it up
		; Into a remainder and quotient for output
		cmp tmp, 9
		jna cont
		sub tmp, 10
		inc j
		jmp subtra
		
	cont:
	
		; Print the tens digit
		mov ah, 02
		mov dl, j
		add dl, 48
		int 21h
		
		; Print the units digit
		mov ah, 02
		mov dl, tmp
		add dl, 48
		int 21h

		; Jump back to calculation procedure
		jmp return
		
	three:
			
		; We must reset j and tmp before multi is called
		mov j, 0
		mov al, sum
		mov tmp, al
		
	multi:
	
		; Divide the number by 100 in order to split it up
		; Into a remainder and quotient for output
		cmp tmp, 99
		jna pretens
		sub tmp, 100
		inc j
		jmp multi
		
	pretens:
	
		; Print the hundreds digit
		mov ah, 02
		mov dl, j
		add dl, 48
		int 21h
		
		; We must reset j before tens is called
		mov j, 0
		
	tens:
	
		; Divide the number by 10 in order to split it up
		; Into a remainder and quotient for output
		cmp tmp, 9
		jna continue
		sub tmp, 10
		inc j
		jmp tens
	
	continue:
	
		; Print the tens digit
		mov ah, 02
		mov dl, j
		add dl, 48
		int 21h
		
		; Print the units digit
		mov ah, 02
		mov dl, tmp
		add dl, 48
		int 21h

		; Jump back to calculation procedure
		jmp return	
		
	exit:
	
		; Back to system - End program
		mov ax, 4c00h
		int 21h

; Indicate that no more commands follow
END