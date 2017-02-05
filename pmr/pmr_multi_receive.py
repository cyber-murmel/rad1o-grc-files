#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: PMR Multi Receive
# Author: marble
# Description: receive multiple PMR channels at once
# Generated: Fri Jul 22 12:48:51 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import threading
import time


class pmr_multi_receive(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "PMR Multi Receive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("PMR Multi Receive")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "pmr_multi_receive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.thres = thres = 160
        self.samp_rate = samp_rate = 0.25e6
        self.cutoff_freq = cutoff_freq = 5e3
        self.chan_width = chan_width = 12.5e3
        self.base_freq = base_freq = 446.0e6+12.5e3
        self.avg_val = avg_val = 0
        self.audio_samp_rate = audio_samp_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self.input_avg = blocks.probe_signal_f()
        self._thres_range = Range(0, 250, 10, 160, 200)
        self._thres_win = RangeWidget(self._thres_range, self.set_thres, "Threshold", "counter_slider", float)
        self.top_layout.addWidget(self._thres_win)
        self._cutoff_freq_range = Range(0.5e3, 10e3, 0.5e3, 5e3, 200)
        self._cutoff_freq_win = RangeWidget(self._cutoff_freq_range, self.set_cutoff_freq, "Cutoff Frequency", "counter_slider", float)
        self.top_layout.addWidget(self._cutoff_freq_win)
        
        def _avg_val_probe():
            while True:
                val = self.input_avg.level()
                try:
                    self.set_avg_val(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _avg_val_thread = threading.Thread(target=_avg_val_probe)
        _avg_val_thread.daemon = True
        _avg_val_thread.start()
            
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(audio_samp_rate),
                decimation=int(samp_rate)/5,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label("Relative Gain", "dB")
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(446e6+6.25e3, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna("", 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	2, samp_rate, 33e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	2, samp_rate, cutoff_freq, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_mute_xx_0 = blocks.mute_ff(bool(avg_val<thres))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0.5, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 1, 4000)
        self.blocks_divide_xx_0_1 = blocks.divide_cc(1)
        self.blocks_divide_xx_0_0_1 = blocks.divide_cc(1)
        self.blocks_divide_xx_0_0_0_1 = blocks.divide_cc(1)
        self.blocks_divide_xx_0_0_0_0 = blocks.divide_cc(1)
        self.blocks_divide_xx_0_0_0 = blocks.divide_cc(1)
        self.blocks_divide_xx_0_0 = blocks.divide_cc(1)
        self.blocks_divide_xx_0 = blocks.divide_cc(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(int(audio_samp_rate), "", True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, chan_width, 1, 0)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate)/5,
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_0_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_0_0_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_0_0_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_0_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_divide_xx_0_1, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_divide_xx_0_0, 0))    
        self.connect((self.blocks_divide_xx_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_divide_xx_0_0, 0), (self.blocks_divide_xx_0_0_0, 0))    
        self.connect((self.blocks_divide_xx_0_0_0, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.blocks_divide_xx_0_0_0, 0), (self.blocks_divide_xx_0_0_0_0, 0))    
        self.connect((self.blocks_divide_xx_0_0_0_0, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.blocks_divide_xx_0_0_0_0, 0), (self.blocks_divide_xx_0_1, 0))    
        self.connect((self.blocks_divide_xx_0_0_0_1, 0), (self.blocks_add_xx_0, 7))    
        self.connect((self.blocks_divide_xx_0_0_1, 0), (self.blocks_add_xx_0, 6))    
        self.connect((self.blocks_divide_xx_0_0_1, 0), (self.blocks_divide_xx_0_0_0_1, 0))    
        self.connect((self.blocks_divide_xx_0_1, 0), (self.blocks_add_xx_0, 5))    
        self.connect((self.blocks_divide_xx_0_1, 0), (self.blocks_divide_xx_0_0_1, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.input_avg, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_mute_xx_0, 0))    
        self.connect((self.blocks_mute_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_divide_xx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pmr_multi_receive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_thres(self):
        return self.thres

    def set_thres(self, thres):
        self.thres = thres
        self.blocks_mute_xx_0.set_mute(bool(self.avg_val<self.thres))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(2, self.samp_rate, 33e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, 1e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate, self.cutoff_freq, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_chan_width(self):
        return self.chan_width

    def set_chan_width(self, chan_width):
        self.chan_width = chan_width
        self.analog_sig_source_x_0.set_frequency(self.chan_width)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq

    def get_avg_val(self):
        return self.avg_val

    def set_avg_val(self, avg_val):
        self.avg_val = avg_val
        self.blocks_mute_xx_0.set_mute(bool(self.avg_val<self.thres))

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate


def main(top_block_cls=pmr_multi_receive, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
