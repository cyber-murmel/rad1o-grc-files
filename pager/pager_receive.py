#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Pager Receive
# Generated: Thu Dec  8 15:14:15 2016
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


class pager_receive(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pager Receive")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pager Receive")
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

        self.settings = Qt.QSettings("GNU Radio", "pager_receive")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.trans_width = trans_width = 30e3
        self.samp_rate = samp_rate = int(2**20)
        self.ppm = ppm = 28
        self.cutoff = cutoff = 70e3
        self.chan_3 = chan_3 = 466.230e6
        self.chan_2 = chan_2 = 466.075e6
        self.chan_1 = chan_1 = 465.970e6
        self.base_freq = base_freq = 466.1e6
        self.audio_rate = audio_rate = int(22.05e3)

        ##################################################
        # Blocks
        ##################################################
        self._ppm_range = Range(-50, 50, 1, 28, 200)
        self._ppm_win = RangeWidget(self._ppm_range, self.set_ppm, 'ppm', "counter_slider", float)
        self.top_layout.addWidget(self._ppm_win)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(466.1e6, 0)
        self.rtlsdr_source_0.set_freq_corr(ppm, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(20, 0)
        self.rtlsdr_source_0.set_if_gain(48, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2**5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=audio_rate,
                decimation=samp_rate/(2**5),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	base_freq, #fc
        	samp_rate, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.02)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2**13, ))
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_short*1, '/dev/stdout', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, 80e3, 180e3, 15e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, base_freq-chan_1, 1, 0)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-70, 1e-4, 0, True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=samp_rate/(2**5),
        	quad_rate=samp_rate/(2**5),
        	tau=75e-6,
        	max_dev=10e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_0, 1))    
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_multiply_xx_0_0_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pager_receive")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_trans_width(self):
        return self.trans_width

    def set_trans_width(self, trans_width):
        self.trans_width = trans_width

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.base_freq, self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 80e3, 180e3, 15e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.rtlsdr_source_0.set_freq_corr(self.ppm, 0)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff

    def get_chan_3(self):
        return self.chan_3

    def set_chan_3(self, chan_3):
        self.chan_3 = chan_3
        self.analog_sig_source_x_0_0_0.set_frequency(self.base_freq-self.chan_3)

    def get_chan_2(self):
        return self.chan_2

    def set_chan_2(self, chan_2):
        self.chan_2 = chan_2
        self.analog_sig_source_x_0_0.set_frequency(self.base_freq-self.chan_2)

    def get_chan_1(self):
        return self.chan_1

    def set_chan_1(self, chan_1):
        self.chan_1 = chan_1
        self.analog_sig_source_x_0.set_frequency(self.base_freq-self.chan_1)

    def get_base_freq(self):
        return self.base_freq

    def set_base_freq(self, base_freq):
        self.base_freq = base_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.base_freq, self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_frequency(self.base_freq-self.chan_3)
        self.analog_sig_source_x_0_0.set_frequency(self.base_freq-self.chan_2)
        self.analog_sig_source_x_0.set_frequency(self.base_freq-self.chan_1)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.audio_rate)


def main(top_block_cls=pager_receive, options=None):

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
