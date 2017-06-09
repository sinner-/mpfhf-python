# mpfhf-python
Python implementation of Mircea Popescu Fabulous Hash Function

## Elements
  * One element is the message to be hashed, M, which is a field of bits of unspecified length.
  * Another element is the so called state machine, S, which starts as one null bit and grows to an unspecified length.
  * The last element is the result of the hashing, R, which is a field of bits of user-specified length. 

## Operations
  * One operation is the bit flip, let it be called `flip`. This operation consists of toggling one specified bit of either S or R.
  * Another operation is the inversion, let it be called `invert`. This operation consists of toggling all the bits of either S or R.
  * A third operation is the flipping of a number of bits in either S or R, let it be called the `screw`. This operation consists of taking the bit count of either S or R, iterating over that value, at each step multiplying the iterator with the current position in M, calculating the remainder of that product against the bit count of R or S respectively, and flipping the remainder-th bit in R or S respectively.
    * `A half-screw` will take half the bit count of S or R instead.
  * The fourth operation is a shift of the state machine, call it `expand`. This operation consists of adding one null bit at the end of S.
  * The last operation is a position rewind, call it a `rewind`. This operation consists of decreasing our position in the message M by one, except in the case our position is already 0.

## Function
  * The function starts by allocating memory : one bit for S, and the size specified by the user for R. All allocated bits are zero.
  * The function starts at position 0 in M and iterates over each bit in M. These iterations are called steps. During each step, the function considers whether the position-th bit in M is 0 or 1, and executes a defined set of operations in either case. Once the operations have been executed, the position is incremented by one. Once the position is larger than the size of M, the function returns R as the hashed value of M.

## Steps
  * if 0, expand and screw S in R. If the bit in R found at the position equal to the remainder of the division of our position in M by the size of R is 0 
    * That bit in R is flipped and we rewind.
    * else, that bit in R is flipped and S is inverted.
  * if 1, half-screw S in R. If the bit in R found at the position equal to the remainder of the division of our position in M by the size of R is equal to the bit in S found at the position equal to the remainder of the division of our position in M by the size of S 
    * We screw S in R.
    * else, that bit in R is flipped.

## Properties
  # The very last bit of M can produce significant change in R, potentially touching all its bits.
  # The fabulous hash-function is message-size indifferent, being operable of messages of any size within the limitations of the hardware only.
  # The fabulous hash-function outputs hashes of any arbitrary length equally well.
  # It is not possible to say, on the basis of a hash, how much memory, or how much CPU was consumed to process the message.
  # The cheapest way to calculate how much memory, or how much CPU will be needed to process a message is to process the message.
  # Because the fabulous hash function does not use blocks, it does not require any kind of padding.
