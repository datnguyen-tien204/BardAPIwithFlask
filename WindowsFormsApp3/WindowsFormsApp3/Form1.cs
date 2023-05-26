using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        private const string ApiUrl = "http://localhost:5000/ask"; // Địa chỉ Flask API

        public Form1()
        {
            InitializeComponent();
        }

        private async void btnAsk_Click(object sender, EventArgs e)
        {
            string question = txtQuestion.Text;

            if (string.IsNullOrEmpty(question))
            {
                MessageBox.Show("Hãy nhập câu hỏi!");
                return;
            }

            try
            {
                using (HttpClient client = new HttpClient())
                {
                    var parameters = new Dictionary<string, string>
                    {
                        { "question", question }
                    };

                    var content = new FormUrlEncodedContent(parameters);

                    // Hiển thị ProgressBar và gửi câu hỏi tới Flask API
                    progress.Minimum = 0;
                    progress.Maximum = 100;
                    progress.Value = 0;

                    var response = await client.PostAsync(ApiUrl, content);
                    var responseContent = await response.Content.ReadAsStringAsync();

                    // Hiển thị câu trả lời trên MessageBox
                    DialogResult result = MessageBox.Show(responseContent, "Câu trả lời", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    if (result == DialogResult.OK)
                    {
                        txtQuestion.Text = "";
                        return;
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Đã xảy ra lỗi: " + ex.Message);
            }
        }

        private void txtAnswer_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtQuestion_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void progress_Click(object sender, EventArgs e)
        {

        }
    }
}
