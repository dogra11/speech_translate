__all__ = ["default_setting", "SettingJson"]
import json
import os
from typing import List

from darkdetect import isDark
from loguru import logger
from notifypy import Notify

from speech_translate._version import __setting_version__
from speech_translate.utils.types import SettingDict

default_setting: SettingDict = {
    "version": __setting_version__,
    "checkUpdateOnStart": True,
    "first_open": True,
    # ------------------ #
    # App settings
    # runtime selection
    "input": "mic",  # mic, speaker
    "transcribe_mw": True,
    "translate_mw": True,
    "transcribe_f_import": True,
    "translate_f_import": True,
    "model_mw": "⛵ Small [2GB VRAM] (Moderate)",
    "model_f_import": "⛵ Small [2GB VRAM] (Moderate)",
    "model_f_alignment": "⛵ Small [2GB VRAM] (Moderate)",
    "model_f_refinement": "⛵ Small [2GB VRAM] (Moderate)",
    "source_lang_mw": "English",
    "target_lang_mw": "Indonesian",
    "source_lang_f_import": "English",
    "target_lang_f_import": "Indonesian",
    "target_lang_f_result": "Indonesian",
    "tl_engine_mw": "Google Translate",
    "tl_engine_f_import": "Google Translate",
    "tl_engine_f_result": "Google Translate",
    "mic": "",
    "speaker": "",
    "hostAPI": "",
    "verbose_record": False,
    "separate_with": "\\n",
    "theme": "sun-valley-dark" if isDark() else "sun-valley-light",
    "show_audio_visualizer_in_record": True,
    "show_audio_visualizer_in_setting": True,
    "supress_hidden_to_tray": False,
    "supress_device_warning": False,
    "supress_record_warning": False,
    "bypass_no_internet": False,
    "mw_size": "1200x600",
    "sw_size": "1100x630",
    "dir_log": "auto",
    "dir_model": "auto",
    "auto_verify_model_on_first_setting_open": False,
    "file_slice_start": "",  # empty will be read as None
    "file_slice_end": "",  # empty will be read as None
    # ------------------ #
    # logging
    "keep_log": False,
    "log_level": "DEBUG",  # INFO DEBUG WARNING ERROR
    "auto_scroll_log": True,
    "auto_refresh_log": True,
    "debug_realtime_record": False,
    "debug_translate": False,
    "debug_recorded_audio": False,
    # ------------------ #
    # Tl Settings
    "https_proxy": "",
    "https_proxy_enable": False,
    "http_proxy": "",
    "http_proxy_enable": False,
    "supress_libre_api_key_warning": False,
    "libre_api_key": "",
    "libre_link": "",
    # ------------------ #
    # Record settings
    "rec_ask_confirmation_first": True,
    # temp
    "use_temp": False,
    "keep_temp": False,
    # mic - device option
    "sample_rate_mic": 16000,
    "channels_mic": "Mono",  # Mono, Stereo, custom -> "1", "2", ...
    "chunk_size_mic": 1024,
    "auto_sample_rate_mic": False,
    "auto_channels_mic": False,
    # mic - record option
    "threshold_enable_mic": True,
    "threshold_auto_mic": True,
    "threshold_auto_silero_mic": True,
    "threshold_silero_mic_min": 0.7,
    "threshold_auto_level_mic": 3,
    "threshold_db_mic": -20.0,
    "auto_break_buffer_mic": True,
    "min_input_length_mic": 0.4,
    "max_buffer_mic": 10,
    "max_sentences_mic": 5,
    "mic_no_limit": False,
    # speaker - device option
    "sample_rate_speaker": 44100,
    "channels_speaker": "Stereo",
    "chunk_size_speaker": 1024,
    "auto_sample_rate_speaker": True,
    "auto_channels_speaker": True,
    # speaker - record option
    "threshold_enable_speaker": True,
    "threshold_auto_speaker": True,
    "threshold_auto_level_speaker": 3,
    "threshold_auto_silero_speaker": True,
    "threshold_silero_speaker_min": 0.7,
    "threshold_db_speaker": -20.0,
    "auto_break_buffer_speaker": True,
    "min_input_length_speaker": 0.4,
    "max_buffer_speaker": 10,
    "max_sentences_speaker": 5,
    "speaker_no_limit": False,
    # Transcribe settings
    "dir_export": "auto",
    "auto_open_dir_export": True,
    "auto_open_dir_refinement": True,
    "auto_open_dir_alignment": True,
    "auto_open_dir_translate": True,
    # counter hallucination
    # rec
    "path_filter_rec": "auto",
    "filter_rec": True,
    "filter_rec_case_sensitive": False,
    "filter_rec_strip": True,
    "filter_rec_ignore_punctuations": "\"',.?!",
    "filter_rec_exact_match": False,
    "filter_rec_similarity": 0.75,
    # file
    "path_filter_file_import": "auto",
    "filter_file_import": True,
    "filter_file_import_case_sensitive": False,
    "filter_file_import_strip": True,
    "filter_file_import_ignore_punctuations": "\"',.?!",
    "filter_file_import_exact_match": True,
    "filter_file_import_similarity": 0.75,
    "remove_repetition_file_import": False,
    "remove_repetition_result_refinement": False,
    "remove_repetition_result_alignment": False,
    "remove_repetition_amount": 1,
    # * Independent
    # {file}
    # {lang-source} {lang-target} {transcribe-with} {translate-with}
    # * In the task only
    # {task} {task-lang} {task-with} {task-lang-with}
    # {task-short} {task-short-lang} {task-short-with} {task-short-lang-with}
    "export_format": "%Y-%m-%d %f {file}/{task-lang}",
    # txt csv json srt ass vtt tsv
    "export_to": ["txt", "srt", "vtt", "json", "ass"],
    "segment_max_words": "",
    "segment_max_chars": "",
    "segment_split_or_newline": "Split",
    "segment_even_split": True,
    "segment_level": True,  # 1 of this must be true
    "word_level": True,  # 1 of this must be true
    "visualize_suppression": False,
    "use_faster_whisper": True,
    "use_en_model": True,
    "transcribe_rate": 300,
    # option for some DecodingOptions that is not available in the command line parameter is moved to the gui
    "decoding_preset": "beam search",  # greedy, beam search, custom
    "temperature": "0.0, 0.2, 0.4, 0.6, 0.8, 1.0",  # 0.0 - 1.0
    "best_of": 3,
    "beam_size": 3,
    "patience": 1.0,
    "compression_ratio_threshold": 2.4,
    "logprob_threshold": -1.0,
    "no_speech_threshold": 0.72,  # Whisper default is 0.6 
    "suppress_tokens": "",  # Whisper default is -1
    "initial_prompt": None,
    "prefix": None,
    "suppress_blank": True,
    "condition_on_previous_text": True,
    "max_initial_timestamp": 1.0,
    "fp16": True,
    "whisper_args": "",
    # ------------------ #
    # Textboxes
    "colorize_per_segment": True,
    "colorize_per_word": False,
    "gradient_low_conf": "#FF0000",
    "gradient_high_conf": "#00FF00",
    # mw tc
    "tb_mw_tc_auto_scroll": True,
    "tb_mw_tc_limit_max": False,
    "tb_mw_tc_limit_max_per_line": False,
    "tb_mw_tc_max": 300,
    "tb_mw_tc_max_per_line": 30,
    "tb_mw_tc_font": "TKDefaultFont",
    "tb_mw_tc_font_bold": False,
    "tb_mw_tc_font_size": 10,
    "tb_mw_tc_use_conf_color": True,
    # mw tl
    "tb_mw_tl_auto_scroll": True,
    "tb_mw_tl_limit_max": False,
    "tb_mw_tl_limit_max_per_line": False,
    "tb_mw_tl_max": 300,
    "tb_mw_tl_max_per_line": 30,
    "tb_mw_tl_font": "TKDefaultFont",
    "tb_mw_tl_font_bold": False,
    "tb_mw_tl_font_size": 10,
    "tb_mw_tl_use_conf_color": True,
    # Tc sub
    "ex_tc_geometry": "800x200",
    "ex_tc_always_on_top": 1,
    "ex_tc_click_through": 0,
    "ex_tc_no_title_bar": 1,
    "ex_tc_no_tooltip": 0,
    "tb_ex_tc_auto_scroll": True,
    "tb_ex_tc_limit_max": False,
    "tb_ex_tc_limit_max_per_line": False,
    "tb_ex_tc_max": 120,
    "tb_ex_tc_max_per_line": 30,
    "tb_ex_tc_font": "Arial",
    "tb_ex_tc_font_bold": True,
    "tb_ex_tc_font_size": 13,
    "tb_ex_tc_font_color": "#FFFFFF",
    "tb_ex_tc_bg_color": "#000000",
    "tb_ex_tc_use_conf_color": True,
    # Tl sub
    "ex_tl_geometry": "800x200",
    "ex_tl_always_on_top": 1,
    "ex_tl_click_through": 0,
    "ex_tl_no_title_bar": 1,
    "ex_tl_no_tooltip": 0,
    "tb_ex_tl_auto_scroll": True,
    "tb_ex_tl_limit_max": False,
    "tb_ex_tl_limit_max_per_line": False,
    "tb_ex_tl_max": 120,
    "tb_ex_tl_max_per_line": 30,
    "tb_ex_tl_font": "Arial",
    "tb_ex_tl_font_bold": True,
    "tb_ex_tl_font_size": 13,
    "tb_ex_tl_font_color": "#FFFFFF",
    "tb_ex_tl_bg_color": "#000000",
    "tb_ex_tl_use_conf_color": True
}


class SettingJson:
    """
    Class to handle setting.json
    """
    def __init__(self, setting_path: str, checkdirs: List[str], path_icon: str):
        logger.debug("Loading setting environment")
        self.cache: SettingDict = {}  # type: ignore
        self.icon_path = path_icon
        self.setting_path = setting_path
        for checkdir in checkdirs:
            self.create_dir_if_not_exist(checkdir)
        self.create_default_setting_if_not_exist()
        logger.debug("Loading setting file")

        # Load setting
        success, msg, data = self.load_setting()
        if success:
            self.cache = data
            # verify loaded setting
            success, msg, data = self.verify_loaded_setting(data)
            if not success:
                self.cache = default_setting
                self.__notify("Error: Verifying setting file", "Setting reverted to default. Details: " + msg)
                logger.warning("Error verifying setting file: " + msg)

            # verify setting version
            if self.cache["version"] != __setting_version__:
                # save old one as backup
                self.save_old_setting(self.cache)
                self.cache = default_setting  # load default
                self.cache["first_open"] = False  # keep first_open to false because it's not first open
                self.save(self.cache)  # save
                msg = "Setting file is outdated. Setting has been reverted to default setting. " \
                    "You can find your old setting in the user folder."
                self.__notify("Setting file is outdated", msg, error=False)
                logger.warning(msg)

            logger.info("Setting loaded")
        else:
            self.cache = default_setting
            logger.error("Error loading setting file: " + msg)
            self.__notify("Error: Loading setting file", "Reason: " + msg)

    def __notify(self, title: str, msg: str, error: bool = True):
        """
        Notify from setting
        """
        notification = Notify()
        notification.application_name = "Speech Translate"
        notification.title = title
        notification.message = msg
        try:
            notification.icon = self.icon_path
        except Exception:
            pass
        notification.send()
        if error:
            logger.error(title)
            logger.error(msg)

    def create_dir_if_not_exist(self, _dir: str):
        """
        Create directory if it doesn't exist
        """
        try:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        except Exception as e:
            self.__notify("Error: Creating directory", "Reason: " + str(e))

    def create_default_setting_if_not_exist(self):
        """
        Create default json file if it doesn't exist
        """
        setting_path = self.setting_path
        try:
            if not os.path.exists(setting_path):
                with open(setting_path, "w", encoding="utf-8") as f:
                    json.dump(default_setting, f, ensure_ascii=False, indent=4)
        except Exception as e:
            logger.exception(e)
            self.__notify("Error: Creating default setting file", "Reason: " + str(e))

    def save(self, data: SettingDict):
        """
        Save json file
        """
        success: bool = False
        msg: str = ""
        try:
            with open(self.setting_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            success = True
            self.cache = data
        except Exception as e:
            msg = str(e)

        return success, msg

    def save_cache(self):
        """
        Save but from cache
        """
        return self.save(self.cache)

    def save_old_setting(self, data: SettingDict):
        """
        Save old setting as backup
        """
        success: bool = False
        msg: str = ""
        try:
            with open(
                self.setting_path.replace("setting.json", f"setting_old_{data['version']}.json"),
                "w",
                encoding="utf-8",
            ) as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            success = True
        except Exception as e:
            msg = str(e)

        return success, msg

    def save_key(self, key: str, value):
        """
        Save setting by key
        """
        if key not in self.cache:
            logger.error(f"Error saving setting: {key}. It's not a valid setting key")
            return
        if self.cache[key] == value:  # if same value
            return

        self.cache[key] = value
        success, msg = self.save(self.cache)

        if not success:
            self.__notify("Error: Saving setting file", "Reason: " + msg)

    def load_setting(self):
        """
        Load json file
        """
        success: bool = False
        msg: str = ""
        data: SettingDict = {}  # type: ignore
        try:
            with open(self.setting_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            success = True
        except Exception as e:
            msg = str(e)

        return success, msg, data

    def verify_loaded_setting(self, data: SettingDict):
        """
        Verify loaded setting
        """
        success: bool = False
        msg: str = ""
        try:
            # check each key
            for key in default_setting:  # pylint: disable=consider-using-dict-items
                if key not in data:
                    data[key] = default_setting[key]

            success = True
        except Exception as e:
            msg = str(e)

        return success, msg, data

    def get_setting(self):
        """
        Get setting value
        """
        return self.cache
