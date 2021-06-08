rule count:
 input: "input/input"
 output: "output/output"
 shell: "wc -w {input} > {output}"

