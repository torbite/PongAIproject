using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameMain : MonoBehaviour
{
    //private AI_bot AI;
    public GameObject ball;
    public GameObject bar1, bar2;
    private Vector2 vel;
    private float hip;
    private int dir = -1;
    public float xBarrier1, xBarrier2;

    void Start()
    {
        Screen.SetResolution(800, 800, false);
        vel = new Vector2(0, dir);
        hip = (bar1.transform.localScale.x / 2) - 0.1f;
        
    }

    // Update is called once per fram
    void Update()
    {
        GetVelocity();
        ball.transform.Translate(vel * Time.deltaTime * 5);
        float hor = Input.GetAxisRaw("Horizontal");
        bar1.transform.Translate(new Vector2(hor,0) * Time.deltaTime * 15);
        bar2.transform.Translate(new Vector2(hor, 0) * Time.deltaTime * 15);
        if((ball.transform.position.x > xBarrier2 && vel.x > 0)||( ball.transform.position.x < xBarrier1 && vel.x < 0))
        {
            vel.x *= -1;
        }
        
    }

    void GetVelocity()
    {
        GameObject bar = (dir == 1) ? bar1 : bar2;

        if (ball.transform.position.x < bar.transform.position.x + hip && ball.transform.position.x > bar.transform.position.x - hip){
            if (ball.transform.position.y < bar.transform.position.y + bar.transform.localScale.y / 2 + 0.3 && ball.transform.position.y > bar.transform.position.y - bar.transform.localScale.y / 2)
            {
                float x = ball.transform.position.x - bar.transform.position.x;
                dir = dir * -1;
                float y = Mathf.Sqrt(Mathf.Pow(hip, 2) - Mathf.Pow(x, 2));
                vel = new Vector2(x, y * dir);
                Debug.Log(vel.x);
                Debug.Log(vel.y);

            }
        }
        
    }
}
