using UnityEngine;
using UnityEngine.Networking;
using System.Collections.Generic;

public class AI_Bot : MonoBehaviour
{
    public int myCode = 0;

    void Start()
    {
        if(myCode == 0)
        {
            int myNewCode = int.Parse(SendGetRequest());
        }
        
    }

    private void Update()
    {
        //string statusCode = SendPostRequest();
        //Debug.Log("result " + statusCode);
    }

    string SendPostRequest(List<float> inputs)
    {
        string url = "http://127.0.0.1:5000";
        //List<int> lista = new List<int> { 1, 2, 3, 4 };
        string jsonBody = JsonUtility.ToJson(inputs);

        UnityWebRequest request = UnityWebRequest.Post(url, "POST");
        byte[] bodyRaw = new System.Text.UTF8Encoding().GetBytes(jsonBody);
        request.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        request.SetRequestHeader("Content-Type", "application/json");

        // Send the request asynchronously
        var operation = request.SendWebRequest();

        // Wait until the operation is done
        while (!operation.isDone) { }

        // Check for network or HTTP errors
        if (request.isNetworkError || request.isHttpError)
        {
            return "Error: " + request.error;
            
        }
        else
        {
            Debug.Log("Request successful!");
            
            return request.downloadHandler.text;

            
        }
    }

    string SendGetRequest()
    {
        string url = "http://127.0.0.1:5000/get_code";
        //List<int> lista = new List<int> { 1, 2, 3, 4 };
        //string jsonBody = JsonUtility.ToJson(inputs);

        //UnityWebRequest request = UnityWebRequest.Post(url, "POST");
        //byte[] bodyRaw = new System.Text.UTF8Encoding().GetBytes(jsonBody);
        //request.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
        //request.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
        //request.SetRequestHeader("Content-Type", "application/json");

        UnityWebRequest request = UnityWebRequest.Get(url);

        // Send the request asynchronously
        var operation = request.SendWebRequest();

        // Wait until the operation is done
        while (!operation.isDone) { }

        // Check for network or HTTP errors
        if (request.isNetworkError || request.isHttpError)
        {
            return "Error: " + request.error;

        }
        else
        {
            Debug.Log("Request successful!");

            return request.downloadHandler.text;


        }
    }


}
