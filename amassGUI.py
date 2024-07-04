import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QPushButton, QLineEdit, QTextEdit, QLabel, QCheckBox, QFileDialog, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt

class AmassGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Amass GUI")
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.intel_tab = QWidget()
        self.enum_tab = QWidget()

        self.tab_widget.addTab(self.intel_tab, "Amass Intel")
        self.tab_widget.addTab(self.enum_tab, "Amass Enum")

        self.create_intel_tab()
        self.create_enum_tab()

    def create_intel_tab(self):
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)

        self.intel_command_output = QTextEdit()
        self.intel_command_output.setMinimumHeight(400)
        self.intel_command_output.setReadOnly(True)

        inner_layout.addWidget(QLabel("Domain:"))
        self.intel_domain_input = QLineEdit()
        inner_layout.addWidget(self.intel_domain_input)

        self.intel_active_check = QCheckBox("Active")
        inner_layout.addWidget(self.intel_active_check)

        inner_layout.addWidget(QLabel("IPs and ranges (comma-separated):"))
        self.intel_addr_input = QLineEdit()
        inner_layout.addWidget(self.intel_addr_input)

        inner_layout.addWidget(QLabel("ASNs (comma-separated):"))
        self.intel_asn_input = QLineEdit()
        inner_layout.addWidget(self.intel_asn_input)

        inner_layout.addWidget(QLabel("CIDRs (comma-separated):"))
        self.intel_cidr_input = QLineEdit()
        inner_layout.addWidget(self.intel_cidr_input)

        inner_layout.addWidget(QLabel("Path to YAML configuration file:"))
        self.intel_config_input = QLineEdit()
        self.intel_config_browse = QPushButton("Browse")
        self.intel_config_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_config_input)
        inner_layout.addWidget(self.intel_config_browse)

        self.intel_demo_check = QCheckBox("Demo")
        inner_layout.addWidget(self.intel_demo_check)

        inner_layout.addWidget(QLabel("Path to a file providing root domain names:"))
        self.intel_df_input = QLineEdit()
        self.intel_df_browse = QPushButton("Browse")
        self.intel_df_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_df_input)
        inner_layout.addWidget(self.intel_df_browse)

        inner_layout.addWidget(QLabel("Path to the directory containing the output files:"))
        self.intel_dir_input = QLineEdit()
        self.intel_dir_browse = QPushButton("Browse")
        self.intel_dir_browse.clicked.connect(self.browse_directory)
        inner_layout.addWidget(self.intel_dir_input)
        inner_layout.addWidget(self.intel_dir_browse)

        inner_layout.addWidget(QLabel("Path to a file providing data sources to exclude:"))
        self.intel_ef_input = QLineEdit()
        self.intel_ef_browse = QPushButton("Browse")
        self.intel_ef_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_ef_input)
        inner_layout.addWidget(self.intel_ef_browse)

        inner_layout.addWidget(QLabel("Data source names separated by commas to be excluded:"))
        self.intel_exclude_input = QLineEdit()
        inner_layout.addWidget(self.intel_exclude_input)

        inner_layout.addWidget(QLabel("Data source names separated by commas to be included:"))
        self.intel_include_input = QLineEdit()
        inner_layout.addWidget(self.intel_include_input)

        self.intel_ip_check = QCheckBox("Show IP addresses for discovered names")
        inner_layout.addWidget(self.intel_ip_check)

        self.intel_ipv4_check = QCheckBox("Show IPv4 addresses for discovered names")
        inner_layout.addWidget(self.intel_ipv4_check)

        self.intel_ipv6_check = QCheckBox("Show IPv6 addresses for discovered names")
        inner_layout.addWidget(self.intel_ipv6_check)

        inner_layout.addWidget(QLabel("Path to the log file where errors will be written:"))
        self.intel_log_input = QLineEdit()
        self.intel_log_browse = QPushButton("Browse")
        self.intel_log_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_log_input)
        inner_layout.addWidget(self.intel_log_browse)

        inner_layout.addWidget(QLabel("Maximum number of concurrent DNS queries:"))
        self.intel_max_dns_queries_input = QLineEdit()
        inner_layout.addWidget(self.intel_max_dns_queries_input)

        inner_layout.addWidget(QLabel("Path to the text file containing terminal stdout/stderr:"))
        self.intel_output_input = QLineEdit()
        self.intel_output_browse = QPushButton("Browse")
        self.intel_output_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_output_input)
        inner_layout.addWidget(self.intel_output_browse)

        inner_layout.addWidget(QLabel("Search string provided against AS description information:"))
        self.intel_org_input = QLineEdit()
        inner_layout.addWidget(self.intel_org_input)

        inner_layout.addWidget(QLabel("Ports separated by commas (default: 80, 443):"))
        self.intel_ports_input = QLineEdit()
        inner_layout.addWidget(self.intel_ports_input)

        inner_layout.addWidget(QLabel("IP addresses of preferred DNS resolvers (comma-separated):"))
        self.intel_resolvers_input = QLineEdit()
        inner_layout.addWidget(self.intel_resolvers_input)

        inner_layout.addWidget(QLabel("Path to a file providing preferred DNS resolvers:"))
        self.intel_rf_input = QLineEdit()
        self.intel_rf_browse = QPushButton("Browse")
        self.intel_rf_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.intel_rf_input)
        inner_layout.addWidget(self.intel_rf_browse)

        inner_layout.addWidget(QLabel("Number of minutes to let enumeration run before quitting:"))
        self.intel_timeout_input = QLineEdit()
        inner_layout.addWidget(self.intel_timeout_input)

        self.intel_verbose_check = QCheckBox("Output status/debug/troubleshooting info")
        inner_layout.addWidget(self.intel_verbose_check)

        self.intel_whois_check = QCheckBox("Run through reverse whois")
        inner_layout.addWidget(self.intel_whois_check)

        self.intel_run_button = QPushButton("Run Amass Intel")
        self.intel_run_button.clicked.connect(self.run_amass_intel)
        inner_layout.addWidget(self.intel_run_button)

        inner_layout.addWidget(self.intel_command_output)

        scroll_area.setWidget(inner_widget)
        layout.addWidget(scroll_area)
        self.intel_tab.setLayout(layout)

    def create_enum_tab(self):
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        inner_widget = QWidget()
        inner_layout = QVBoxLayout(inner_widget)

        self.enum_command_output = QTextEdit()
        self.enum_command_output.setMinimumHeight(400)
        self.enum_command_output.setReadOnly(True)

        inner_layout.addWidget(QLabel("Domain:"))
        self.enum_domain_input = QLineEdit()
        inner_layout.addWidget(self.enum_domain_input)

        self.enum_active_check = QCheckBox("Active")
        inner_layout.addWidget(self.enum_active_check)

        self.enum_alts_check = QCheckBox("Enable generation of altered names")
        inner_layout.addWidget(self.enum_alts_check)

        self.enum_brute_check = QCheckBox("Execute brute forcing after searches")
        inner_layout.addWidget(self.enum_brute_check)

        inner_layout.addWidget(QLabel("IPs and ranges (comma-separated):"))
        self.enum_addr_input = QLineEdit()
        inner_layout.addWidget(self.enum_addr_input)

        inner_layout.addWidget(QLabel("ASNs (comma-separated):"))
        self.enum_asn_input = QLineEdit()
        inner_layout.addWidget(self.enum_asn_input)

        inner_layout.addWidget(QLabel("CIDRs (comma-separated):"))
        self.enum_cidr_input = QLineEdit()
        inner_layout.addWidget(self.enum_cidr_input)

        inner_layout.addWidget(QLabel("Path to different wordlist file for alterations:"))
        self.enum_aw_input = QLineEdit()
        self.enum_aw_browse = QPushButton("Browse")
        self.enum_aw_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_aw_input)
        inner_layout.addWidget(self.enum_aw_browse)

        inner_layout.addWidget(QLabel("Hashcat-style wordlist masks for name alterations:"))
        self.enum_awm_input = QLineEdit()
        inner_layout.addWidget(self.enum_awm_input)

        inner_layout.addWidget(QLabel("Blacklist of subdomain names:"))
        self.enum_bl_input = QLineEdit()
        inner_layout.addWidget(self.enum_bl_input)

        inner_layout.addWidget(QLabel("Path to file providing blacklisted subdomains:"))
        self.enum_blf_input = QLineEdit()
        self.enum_blf_browse = QPushButton("Browse")
        self.enum_blf_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_blf_input)
        inner_layout.addWidget(self.enum_blf_browse)

        inner_layout.addWidget(QLabel("Path to YAML configuration file:"))
        self.enum_config_input = QLineEdit()
        self.enum_config_browse = QPushButton("Browse")
        self.enum_config_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_config_input)
        inner_layout.addWidget(self.enum_config_browse)

        self.enum_demo_check = QCheckBox("Demo")
        inner_layout.addWidget(self.enum_demo_check)

        inner_layout.addWidget(QLabel("Path to file providing root domain names:"))
        self.enum_df_input = QLineEdit()
        self.enum_df_browse = QPushButton("Browse")
        self.enum_df_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_df_input)
        inner_layout.addWidget(self.enum_df_browse)

        inner_layout.addWidget(QLabel("Path to directory containing output files:"))
        self.enum_dir_input = QLineEdit()
        self.enum_dir_browse = QPushButton("Browse")
        self.enum_dir_browse.clicked.connect(self.browse_directory)
        inner_layout.addWidget(self.enum_dir_input)
        inner_layout.addWidget(self.enum_dir_browse)

        inner_layout.addWidget(QLabel("Maximum DNS queries per second across all resolvers:"))
        self.enum_dns_qps_input = QLineEdit()
        inner_layout.addWidget(self.enum_dns_qps_input)

        inner_layout.addWidget(QLabel("Path to file providing data sources to exclude:"))
        self.enum_ef_input = QLineEdit()
        self.enum_ef_browse = QPushButton("Browse")
        self.enum_ef_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_ef_input)
        inner_layout.addWidget(self.enum_ef_browse)

        inner_layout.addWidget(QLabel("Data source names to exclude (comma-separated):"))
        self.enum_exclude_input = QLineEdit()
        inner_layout.addWidget(self.enum_exclude_input)

        inner_layout.addWidget(QLabel("Data source names to include (comma-separated):"))
        self.enum_include_input = QLineEdit()
        inner_layout.addWidget(self.enum_include_input)

        self.enum_ip_check = QCheckBox("Show IP addresses for discovered names")
        inner_layout.addWidget(self.enum_ip_check)

        self.enum_ipv4_check = QCheckBox("Show IPv4 addresses for discovered names")
        inner_layout.addWidget(self.enum_ipv4_check)

        self.enum_ipv6_check = QCheckBox("Show IPv6 addresses for discovered names")
        inner_layout.addWidget(self.enum_ipv6_check)

        inner_layout.addWidget(QLabel("Path to log file for errors:"))
        self.enum_log_input = QLineEdit()
        self.enum_log_browse = QPushButton("Browse")
        self.enum_log_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_log_input)
        inner_layout.addWidget(self.enum_log_browse)

        inner_layout.addWidget(QLabel("Max concurrent DNS queries per second:"))
        self.enum_max_dns_queries_input = QLineEdit()
        inner_layout.addWidget(self.enum_max_dns_queries_input)

        inner_layout.addWidget(QLabel("Path to text file for terminal stdout/stderr:"))
        self.enum_output_input = QLineEdit()
        self.enum_output_browse = QPushButton("Browse")
        self.enum_output_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_output_input)
        inner_layout.addWidget(self.enum_output_browse)

        inner_layout.addWidget(QLabel("Search string for AS description information:"))
        self.enum_org_input = QLineEdit()
        inner_layout.addWidget(self.enum_org_input)

        inner_layout.addWidget(QLabel("Ports to check (comma-separated):"))
        self.enum_ports_input = QLineEdit()
        inner_layout.addWidget(self.enum_ports_input)

        inner_layout.addWidget(QLabel("IP addresses of preferred DNS resolvers (comma-separated):"))
        self.enum_resolvers_input = QLineEdit()
        inner_layout.addWidget(self.enum_resolvers_input)

        inner_layout.addWidget(QLabel("Path to file providing preferred DNS resolvers:"))
        self.enum_rf_input = QLineEdit()
        self.enum_rf_browse = QPushButton("Browse")
        self.enum_rf_browse.clicked.connect(self.browse_file)
        inner_layout.addWidget(self.enum_rf_input)
        inner_layout.addWidget(self.enum_rf_browse)

        inner_layout.addWidget(QLabel("Timeout in minutes:"))
        self.enum_timeout_input = QLineEdit()
        inner_layout.addWidget(self.enum_timeout_input)

        self.enum_verbose_check = QCheckBox("Output status/debug info")
        inner_layout.addWidget(self.enum_verbose_check)

        self.enum_whois_check = QCheckBox("Run through reverse whois")
        inner_layout.addWidget(self.enum_whois_check)

        self.enum_run_button = QPushButton("Run Amass Enum")
        self.enum_run_button.clicked.connect(self.run_amass_enum)
        inner_layout.addWidget(self.enum_run_button)

        inner_layout.addWidget(self.enum_command_output)

        scroll_area.setWidget(inner_widget)
        layout.addWidget(scroll_area)
        self.enum_tab.setLayout(layout)

    def browse_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if file_path:
            sender = self.sender()
            if sender == self.intel_config_browse:
                self.intel_config_input.setText(file_path)
            elif sender == self.intel_df_browse:
                self.intel_df_input.setText(file_path)
            elif sender == self.intel_ef_browse:
                self.intel_ef_input.setText(file_path)
            elif sender == self.intel_log_browse:
                self.intel_log_input.setText(file_path)
            elif sender == self.intel_output_browse:
                self.intel_output_input.setText(file_path)
            elif sender == self.intel_rf_browse:
                self.intel_rf_input.setText(file_path)
            elif sender == self.enum_aw_browse:
                self.enum_aw_input.setText(file_path)
            elif sender == self.enum_blf_browse:
                self.enum_blf_input.setText(file_path)
            elif sender == self.enum_config_browse:
                self.enum_config_input.setText(file_path)
            elif sender == self.enum_df_browse:
                self.enum_df_input.setText(file_path)
            elif sender == self.enum_ef_browse:
                self.enum_ef_input.setText(file_path)
            elif sender == self.enum_log_browse:
                self.enum_log_input.setText(file_path)
            elif sender == self.enum_output_browse:
                self.enum_output_input.setText(file_path)
            elif sender == self.enum_rf_browse:
                self.enum_rf_input.setText(file_path)

    def browse_directory(self):
        options = QFileDialog.Options()
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory", "", options=options)
        if dir_path:
            sender = self.sender()
            if sender == self.intel_dir_browse:
                self.intel_dir_input.setText(dir_path)
            elif sender == self.enum_dir_browse:
                self.enum_dir_input.setText(dir_path)

    def run_amass_intel(self):
        try:
            command = ["amass", "intel"]

            if self.intel_domain_input.text():
                command.extend(["-d", self.intel_domain_input.text()])
            if self.intel_active_check.isChecked():
                command.append("-active")
            if self.intel_addr_input.text():
                command.extend(["-addr", self.intel_addr_input.text()])
            if self.intel_asn_input.text():
                command.extend(["-asn", self.intel_asn_input.text()])
            if self.intel_cidr_input.text():
                command.extend(["-cidr", self.intel_cidr_input.text()])
            if self.intel_config_input.text():
                command.extend(["-config", self.intel_config_input.text()])
            if self.intel_demo_check.isChecked():
                command.append("-demo")
            if self.intel_df_input.text():
                command.extend(["-df", self.intel_df_input.text()])
            if self.intel_dir_input.text():
                command.extend(["-dir", self.intel_dir_input.text()])
            if self.intel_ef_input.text():
                command.extend(["-ef", self.intel_ef_input.text()])
            if self.intel_exclude_input.text():
                command.extend(["-exclude", self.intel_exclude_input.text()])
            if self.intel_include_input.text():
                command.extend(["-include", self.intel_include_input.text()])
            if self.intel_ip_check.isChecked():
                command.append("-ip")
            if self.intel_ipv4_check.isChecked():
                command.append("-ipv4")
            if self.intel_ipv6_check.isChecked():
                command.append("-ipv6")
            if self.intel_log_input.text():
                command.extend(["-log", self.intel_log_input.text()])
            if self.intel_max_dns_queries_input.text():
                command.extend(["-max-dns-queries", self.intel_max_dns_queries_input.text()])
            if self.intel_output_input.text():
                command.extend(["-o", self.intel_output_input.text()])
            if self.intel_org_input.text():
                command.extend(["-org", self.intel_org_input.text()])
            if self.intel_ports_input.text():
                command.extend(["-ports", self.intel_ports_input.text()])
            if self.intel_resolvers_input.text():
                command.extend(["-r", self.intel_resolvers_input.text()])
            if self.intel_rf_input.text():
                command.extend(["-rf", self.intel_rf_input.text()])
            if self.intel_timeout_input.text():
                command.extend(["-timeout", self.intel_timeout_input.text()])
            if self.intel_verbose_check.isChecked():
                command.append("-v")
            if self.intel_whois_check.isChecked():
                command.append("-whois")

            self.intel_command_output.append("Running: " + " ".join(command))
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.intel_command_output.append(result.stdout.decode())
            self.intel_command_output.append(result.stderr.decode())
        except Exception as e:
            self.intel_command_output.append(f"Error: {str(e)}")

    def run_amass_enum(self):
        try:
            command = ["amass", "enum"]

            if self.enum_domain_input.text():
                command.extend(["-d", self.enum_domain_input.text()])
            if self.enum_active_check.isChecked():
                command.append("-active")
            if self.enum_alts_check.isChecked():
                command.append("-alts")
            if self.enum_brute_check.isChecked():
                command.append("-brute")
            if self.enum_addr_input.text():
                command.extend(["-addr", self.enum_addr_input.text()])
            if self.enum_asn_input.text():
                command.extend(["-asn", self.enum_asn_input.text()])
            if self.enum_cidr_input.text():
                command.extend(["-cidr", self.enum_cidr_input.text()])
            if self.enum_aw_input.text():
                command.extend(["-aw", self.enum_aw_input.text()])
            if self.enum_awm_input.text():
                command.extend(["-awm", self.enum_awm_input.text()])
            if self.enum_bl_input.text():
                command.extend(["-bl", self.enum_bl_input.text()])
            if self.enum_blf_input.text():
                command.extend(["-blf", self.enum_blf_input.text()])
            if self.enum_config_input.text():
                command.extend(["-config", self.enum_config_input.text()])
            if self.enum_demo_check.isChecked():
                command.append("-demo")
            if self.enum_df_input.text():
                command.extend(["-df", self.enum_df_input.text()])
            if self.enum_dir_input.text():
                command.extend(["-dir", self.enum_dir_input.text()])
            if self.enum_dns_qps_input.text():
                command.extend(["-dns-qps", self.enum_dns_qps_input.text()])
            if self.enum_ef_input.text():
                command.extend(["-ef", self.enum_ef_input.text()])
            if self.enum_exclude_input.text():
                command.extend(["-exclude", self.enum_exclude_input.text()])
            if self.enum_include_input.text():
                command.extend(["-include", self.enum_include_input.text()])
            if self.enum_ip_check.isChecked():
                command.append("-ip")
            if self.enum_ipv4_check.isChecked():
                command.append("-ipv4")
            if self.enum_ipv6_check.isChecked():
                command.append("-ipv6")
            if self.enum_log_input.text():
                command.extend(["-log", self.enum_log_input.text()])
            if self.enum_max_dns_queries_input.text():
                command.extend(["-max-dns-queries", self.enum_max_dns_queries_input.text()])
            if self.enum_output_input.text():
                command.extend(["-o", self.enum_output_input.text()])
            if self.enum_org_input.text():
                command.extend(["-org", self.enum_org_input.text()])
            if self.enum_ports_input.text():
                command.extend(["-ports", self.enum_ports_input.text()])
            if self.enum_resolvers_input.text():
                command.extend(["-r", self.enum_resolvers_input.text()])
            if self.enum_rf_input.text():
                command.extend(["-rf", self.enum_rf_input.text()])
            if self.enum_timeout_input.text():
                command.extend(["-timeout", self.enum_timeout_input.text()])
            if self.enum_verbose_check.isChecked():
                command.append("-v")
            if self.enum_whois_check.isChecked():
                command.append("-whois")

            self.enum_command_output.append("Running: " + " ".join(command))
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.enum_command_output.append(result.stdout.decode())
            self.enum_command_output.append(result.stderr.decode())
        except Exception as e:
            self.enum_command_output.append(f"Error: {str(e)}")


if __name__ == "__main__":
    app = QApplication([])
    window = AmassGUI()
    window.show()
    app.exec_()
