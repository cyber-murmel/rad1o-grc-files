#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Broadcast Udp
# Generated: Mon Dec 26 22:44:38 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr


class broadcast_udp(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Broadcast Udp")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = int(1e6)
        self.base_freq = base_freq = 101.11e6
        self.audio_rate = audio_rate = int(48e3)

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=10*audio_rate,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(base_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(47, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_short*1, 'localhost', 1337, int(10e6), True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((50/(1e6), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.75, ))
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=10*audio_rate,
        	tau=75e-6,
        	max_dev=30e3,
        	fh=-1.0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_short_to_float_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self.osmosdr_sink_0.set_center_freq(self.base_freq, 0)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate


def main(top_block_cls=broadcast_udp, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
