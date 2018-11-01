from myhdl import *
from random import randrange

def dff(q, d, clk):

    @always(clk.posedge)
    def logic():
        q.next = d

    return logic


def testbench():

    q, d, clk = [Signal(bool(0)) for i in range(3)]

    dff_inst = dff(q, d, clk)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.negedge)
    def stimulus():
        d.next = randrange(2)

    return dff_inst, clkgen, stimulus



tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()

