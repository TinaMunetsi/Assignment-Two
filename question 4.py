# A 50GB CSV file cannot be loaded directly into RAM because
# doing so can cause an OutOfMemoryError.
#
# A memory-efficient solution is to use a Python generator.
#
# A generator produces values one at a time instead of storing
# all values in memory at once.
#
# The function below reads the file lazily in chunks whose size
# is controlled by chunk_size_bytes.
#
# A buffer is maintained between chunks so that a line that
# starts in one chunk and continues into the next chunk is not
# split into two separate lines.
#
# Only the required chunk and incomplete line are kept in
# memory, rather than the entire file.
#
# This means the function can process very large files while
# keeping the memory footprint relatively small.


def chunked_file_reader(file_path, chunk_size_bytes):
    """
    Read a text file lazily in chunks and yield complete lines.

    Lines that cross chunk boundaries are combined before
    being yielded.
    """

   
    with open(file_path, "r", encoding="utf-8", newline="") as file:

        # Store any incomplete line from the previous chunk.
        remainder = ""

        while True:

            # Read only the requested number of characters.
            chunk = file.read(chunk_size_bytes)

            # Stop when the end of the file is reached.
            if not chunk:
                break

            # Add the new chunk to any incomplete line from
            # the previous chunk.
            data = remainder + chunk

            # Split the data into lines.
            lines = data.splitlines(keepends=True)

            # If there are no lines, continue reading.
            if not lines:
                remainder = data
                continue

            # Check whether the final element contains a
            # complete line.
            if lines[-1].endswith(("\n", "\r")):
                remainder = ""

                # All lines are complete, so yield them.
                for line in lines:
                    yield line.rstrip("\r\n")

            else:
                # The final element does not contain a newline,
                # so it may be an incomplete line.
                remainder = lines.pop()

                # Yield all complete lines.
                for line in lines:
                    yield line.rstrip("\r\n")

        # After the file has been completely read, yield any
        # remaining text as the final line.
        if remainder:
            yield remainder.rstrip("\r\n")


# ------------------------------------------------------------
# Example usage of the generator
# ------------------------------------------------------------



# A chunk size of 1MB is used in this example.
#
# The generator does not load the complete CSV file into RAM.

file_path = "Tinotenda_file.csv"
chunk_size = 1024 * 1024  # 1 MB

# The file is processed one line at a time.

# for line in chunked_file_reader(file_path, chunk_size):
#     print(line)
